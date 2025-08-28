# Analyse Deaths Involving Police in the United States

A Python-based **data analysis and visualisation project** focusing on deaths involving police officers in the United States.  
The project collects, cleans, and analyses open-source datasets to identify **patterns, trends, demographics, and geospatial insights** about police-related fatalities.

---

## Table of Contents

- [Description](#description)
- [Key Questions](#key-questions)
- [Features](#features)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Visualisations](#visualisations)
- [Ethical Considerations](#ethical-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Description

This project provides a data-driven exploration of **police-involved deaths in the U.S.**  
It aims to highlight **trends over time, geographic distributions, racial/ethnic disparities, causes of death, and case outcomes**.  

The focus is not only on descriptive statistics but also on **patterns that can inform policy, journalism, and academic research**.

---

## Key Questions

- What is the **yearly trend** of police-involved deaths in the U.S.?  
- What are the **demographic breakdowns** (age, gender, race/ethnicity) of victims?  
- Which **states and counties** report the highest rates per capita?  
- How do **circumstances of death** (e.g., gunfire, restraints, taser, vehicle) vary?  
- How often are officers **charged or convicted** in such incidents?  
- What are the correlations with **socio-economic or crime rate indicators**?  

---

## Features

- **ETL pipeline** for ingesting multiple datasets (CSV, API, JSON)  
- **Data cleaning & standardisation** (race categories, cause of death, geocoding)  
- **Descriptive & comparative analysis** (time, geography, demographics)  
- **Interactive dashboards** using Plotly Dash / Streamlit  
- **Geospatial visualisation** with maps of incidents (choropleths, heatmaps)  
- **Per capita rate calculations** using Census population data  
- **Export tools** for charts, datasets, and summaries  

---

## Data Sources

> Public and journalistic datasets, e.g.:
- [Fatal Encounters Database](https://fatalencounters.org/)  
- [The Washington Post – Police Shootings Database](https://github.com/washingtonpost/data-police-shootings)  
- [Mapping Police Violence](https://mappingpoliceviolence.us/)  
- [US Census Bureau Data](https://data.census.gov/) for population denominators  

*(Ensure licensing/permissions for the datasets you select — store metadata in `data/sources.md`.)*

---

## Requirements

- Python 3.9+  
- Libraries:
  - Data: `pandas`, `numpy`, `python-dateutil`
  - Viz: `matplotlib`, `seaborn`, `plotly`, `altair`
  - Geo: `geopandas`, `folium`, `shapely`
  - API/IO: `requests`, `pyyaml`
  - Dashboard: `dash` or `streamlit`
  - Dev: `jupyter`, `black`, `isort`, `pre-commit`

Install:
```bash
pip install -r requirements.txt
```

---

## Installation

```bash
git clone https://github.com/yourusername/police-deaths-analysis.git
cd police-deaths-analysis
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Quick Start

```bash
make all
# or
python -m src.cli ingest --from data/raw
python -m src.cli clean
python -m src.cli build-charts
python -m src.cli serve-dashboard
```

Dashboard will be available at:
```
http://127.0.0.1:8050/
```

---

## Usage

### 1) Ingest Data
```bash
python -m src.cli ingest --from data/raw/fatal_encounters.csv
```

### 2) Clean Data
```bash
python -m src.cli clean --map race_map.csv --map cause_map.csv
```

### 3) Run EDA Notebook
```bash
jupyter lab notebooks/01_exploratory_analysis.ipynb
```

### 4) Visualise & Serve Dashboard
```bash
python -m src.cli serve-dashboard
```

---

## Project Structure

```
police-deaths-analysis/
├── data/
│   ├── raw/              # Original datasets
│   ├── interim/          # Staged, cleaned versions
│   ├── processed/        # Final ready-to-analyse datasets
│   └── reference/        # Mapping files (race categories, census)
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_demographics.ipynb
│   ├── 03_geospatial.ipynb
│   └── 04_time_trends.ipynb
├── reports/
│   ├── figures/          # Static plots
│   └── dashboard/        # Interactive outputs
├── src/
│   ├── cli.py            # CLI tool with Typer
│   ├── etl/
│   │   ├── ingest.py
│   │   ├── clean.py
│   │   └── validate.py
│   ├── analysis/
│   │   ├── demographics.py
│   │   ├── geography.py
│   │   └── trends.py
│   └── viz/
│       ├── charts.py
│       ├── maps.py
│       └── dashboard.py
├── requirements.txt
├── Makefile
└── README.md
```

---

## Data Model

**Table: `incidents` (analysis-ready)**  
- `incident_id` (unique ID)  
- `date` (datetime)  
- `state`, `county`, `city`  
- `latitude`, `longitude`  
- `victim_age`, `victim_gender`, `victim_race`  
- `cause_of_death` (gunfire, taser, restraint, vehicle, other)  
- `armed_status` (armed/unarmed/unknown)  
- `officer_charged` (yes/no/unknown)  
- `agency` (police dept, sheriff, state patrol, federal)  

**Table: `population` (for per capita rates)**  
- `state`, `county`, `year`, `population_total`, `population_race_breakdown`

---

## Visualisations

- **Trend lines** of total deaths per year and per 100,000 population  
- **Bar charts** by race, gender, age groups  
- **Heatmaps** by state and per capita rates  
- **Geospatial maps**: incident density, hotspot analysis  
- **Stacked bars** by cause of death and armed status  
- **Comparisons** across agencies and regions  

---

## Ethical Considerations

- **Data sensitivity**: These represent real human lives. Handle with care.  
- **Bias in datasets**: Not all deaths are reported/recorded equally; gaps exist.  
- **Privacy**: Remove personally identifying information (PII) from public outputs.  
- **Purpose**: The goal is **analysis and awareness**, not sensationalism.  

---

## Minimal Example

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/processed/incidents.csv")
trend = df.groupby(df['date'].str[:4]).size().reset_index(name="deaths")

fig = px.line(trend, x="date", y="deaths", title="Police-Involved Deaths Per Year")
fig.show()
```

---

## Contributing

Contributions are welcome!  
- Add new datasets (with source + license)  
- Improve data cleaning/mapping scripts  
- Build new visualisations or metrics  
- Suggest ethical safeguards or context notes  

Steps:
1. Fork repo  
2. Create branch (`feature-race-analysis`)  
3. Commit & push  
4. Open Pull Request  

---

## License

This project is licensed under the **MIT License**.  
Note: Dataset licensing may vary — check `data/sources.md` for dataset-specific terms.

---
