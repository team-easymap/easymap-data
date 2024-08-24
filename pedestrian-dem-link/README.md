# easymap-data / pedestrian-dem-link

## 원천 데이터
- [pedestrian-node-link-seoul](../pedestrian-node-link-seoul/README.md)
- DEM
  - 수치표고모델 90M
    - https://www.vworld.kr/dtmk/dtmk_ntads_s002.do?svcCde=MK&dsId=30206
  - 연속수치지형도 1:5000 등고선
    - https://www.vworld.kr/dtmk/dtmk_ntads_s002.do?svcCde=MK&dsId=30185
  - ~~수치지형도V1 1:1000~~
    - [~~https://map.ngii.go.kr/ms/map/NlipMap.do~~](https://map.ngii.go.kr/ms/map/NlipMap.do)
  - ~~수치지형도V2 1:1000~~
    - [~~https://map.ngii.go.kr/ms/map/NlipMap.do~~](https://map.ngii.go.kr/ms/map/NlipMap.do)


## 프로세스
- 도보네트워크 링크 → 라인분해 → 도보네트워크 단위링크 (41.9만)
- 도보네트워크 단위링크 → 꼭짓점 추출 → 도보네트워크 단위링크 꼭짓점 (83.9만)
- 도보네트워크 단위노드 + DEM → 도보네트워크 단위링크 표고점
- 도보네트워크 단위링크 표고점 + 도보네트워크 단위링크 → 도보네트워크 단위링크 경사도 통계 (uniq count, min, max, median, avg)
- 도보네트워크 단위링크 경사도 통계 → 도보네트워크 링크 1:N 속성 결합 → 도보네트워크 링크 + 링크별 경사도 통계


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

### etl-pg

```bash
python load-to-pg.py
```
