import polars as pl

df = pl.scan_csv('data/arxiv-metadata-oai-snapshot.json')
df.select(pl.col('versions'))