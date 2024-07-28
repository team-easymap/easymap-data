# easymap-data / pedestrian-node-link-seoul

## 원천 데이터
- https://data.seoul.go.kr/dataList/OA-21208/S/1/datasetView.do


## setup

```bash
python -m venv ./.venv
source .venv/bin/activate

pip install psycopg2-binary

pythoon load-to-pg.py
```


## etl-mysql

```bash
python -m venv ./.venv
source .venv/bin/activate

pip install mysql-connector-python

pythoon load-to-mysql.py
```
