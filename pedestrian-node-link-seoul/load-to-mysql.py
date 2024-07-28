import csv
import mysql.connector
from mysql.connector import Error
import time

def chunk(list, size):
    for i in range(0, len(list), size):
        yield list[i:i + size]
    
def bulk_insert(connection, cursor, data_list, query):
    affected_rows = 0
    for data_chunk in chunk(data_list, 1000):
        cursor.executemany(query, data_chunk)
        connection.commit()  # 각 청크 삽입 후 커밋
        
        time.sleep(0.1)  # 100ms 대기
        affected_rows += len(data_chunk)
        print(f"Affected rows: {affected_rows}")

def main():
    try:
        node_data_list = []
        link_data_list = []

        # Open and read the CSV file
        with open('data.csv', mode='r', encoding='cp949') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['노드링크 유형'] == 'NODE':
                    node_data_list.append((
                        row['노드링크 유형'],
                        row['노드 WKT'],
                        row['노드 ID'],
                        row['노드 유형 코드'],
                        row['시군구코드'],
                        row['시군구명'],
                        row['읍면동코드'],
                        row['읍면동명'],
                        row['육교'],
                        row['횡단보도'],
                    ))
                elif row['노드링크 유형'] == 'LINK':
                    link_data_list.append((
                        row['노드링크 유형'],
                        row['링크 WKT'],
                        row['링크 ID'],
                        row['링크 유형 코드'],
                        row['시작노드 ID'],
                        row['종료노드 ID'],
                        row['링크 길이'],
                        row['시군구코드'],
                        row['시군구명'],
                        row['읍면동코드'],
                        row['읍면동명'],
                        row['고가도로'],
                        row['지하철네트워크'],
                        row['교량'],
                        row['터널'],
                        row['육교'],
                        row['횡단보도'],
                        row['공원,녹지'],
                        row['건물내'],
                    ))

        print('node_data_list:', len(node_data_list))
        print('link_data_list:', len(link_data_list))

        # Connect to the database
        db_config = {
            'host': '',
            'user': '',
            'password': '',
            'database': ''
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # chunk_size 만큼씩 데이터를 삽입
        print("bulk_insert start :: raw.node_data ")
        bulk_insert(
            connection,
            cursor,
            node_data_list,
            """
            INSERT INTO raw.node_data (type, node_wkt, node_id, node_code, sgg_cd, sgg_nm, emd_cd, emd_nm, tp_sw, tp_cw)
            VALUES (%s, ST_PointFromText(%s), %s, %s, %s, %s, %s, %s, %s, %s)
            """)
        print("bulk_insert end :: raw.node_data ")

        print("bulk_insert start :: raw.link_data ")
        bulk_insert(
            connection,
            cursor, 
            link_data_list,
            """
            INSERT INTO raw.link_data (type, link_wkt, link_id, link_code, strt_node_id, end_node_id, link_len, sgg_cd, sgg_nm, emd_cd, emd_nm, tp_hw, tp_uw, tp_br, tp_tn, tp_sw, tp_cw, tp_pk, tp_in)
            VALUES (%s, ST_LineStringFromText(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """)
        print("bulk_insert end :: raw.link_data ")

        # Commit the transactions
        connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    main()
