# IDs Scraper

[Calendarium](https://calendario.cesium.di.uminho.pt/) uses a subject ID and a filterID. The first is given by the university, the second is calculated with:

```python
filterId = f"{university_year}{university_semester}{subject_code}"
```

Where the subject code is the position of the subject in a alphabetic ordered list. For example:

```python
# 1st year & 1st semester subjects:
["Álgebra", "Cálculo", "Tópicos Matemática"]
```

The `filterID` of `Tópicos Matemática` will be `113`.

## Scraping this values

On the 1st year of [Calendarium](https://calendario.cesium.di.uminho.pt/) all subjects IDs were scraped manually and all subjectIds calculated, so now we just have to scrap them from [shifts.json](https://github.com/cesium/calendarium/blob/96169aac3d6771e3eb27c1f782a204fe85ba682c/data/shifts.json) from that time.

Some information of my scraped shifts are lightly different from the manual scrap (ex.: "Cálculo para a Engenharia" and "Cálculo para Engenharia" are the same subject but with a little different name) so we need to fix it on the script.

Also, some subjects were not scraped manually (`Opções UMinho`), so we need to add them, also manually, on the script.

### Running

From the root directory of the project run:

```bash
python ids_scraper/ids_scraper.py
```

The scrape will be stored at `ids.json`.
