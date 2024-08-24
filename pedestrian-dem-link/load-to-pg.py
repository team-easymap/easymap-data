from dotenv import load_dotenv
import os
import geopandas as gpd
from sqlalchemy import create_engine

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

data = [
    ('./data/pedestrian_unit_link_dem.gpkg', 'pedestrian_unit_link_dem'),
    ('./data/pedestrian_unit_link.gpkg', 'pedestrian_unit_link'),
]

for gpkg_file, layer_name in data:
    df = gpd.read_file(gpkg_file, layer=layer_name)
    print(f'read {gpkg_file} ok')
    
    table_name = layer_name
    gdf.to_postgis(table_name, engine, if_exists='replace')
    print(f'Data from {gpkg_file} has been successfully imported into {table_name}.')
