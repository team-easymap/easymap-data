# easymap-data / pedestrian-obstacles-seoul

## 원천 데이터
- 스마트 서울맵 보행약자 안전 이동경로
  - https://map.seoul.go.kr/smgis2/themeGallery/detail?theme_id=1694517815685

## setup

```bash
python3 -m venv ./.venv
source .venv/bin/activate

pip install geopandas sqlalchemy geoalchemy2 psycopg2-binary jupyterlab python-dotenv
```

### EDA

```bash
jupyter lab
```
