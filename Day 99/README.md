# Analyse and Visualise the Space Race

A Python data project to **analyse, compare, and visualise milestones of the Space Race** — from early Cold War launches to the modern commercial era.  
It includes data ingestion, cleaning, exploratory analysis, and rich visualisations (timelines, maps, trend lines, rankings, and network graphs).

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
- [Reproducibility](#reproducibility)
- [Contributing](#contributing)
- [License](#license)

---

## Description

This project curates launch and mission data to uncover trends across nations, agencies, and companies throughout the Space Race era and beyond.  
It focuses on **launch cadence**, **success rates**, **payload capabilities**, **orbits**, **program milestones**, and **collaboration networks**.

---

## Key Questions

- How did **launch frequency** evolve by country/agency from the 1950s to today?  
- What are the **success/failure rates** across launch vehicles and time?  
- How do **payload masses** and **target orbits** (LEO/MEO/GEO/HEO) change over decades?  
- Which agencies/companies dominate certain orbits or mission types?  
- What are the pivotal **milestones** (first satellite, human spaceflight, Moon landing, reusable rockets, private crewed flights)?  
- How did **international cooperation** (e.g., ISS) reshape activity?

---

## Features

- **ETL pipeline** to ingest CSV/JSON sources into a clean, unified schema  
- **Data quality checks** (dedupe launches, normalize agency/country names, validate dates/orbits)  
- **Exploratory Data Analysis (EDA)** notebooks with reusable helper functions  
- **Interactive dashboards** (Plotly/Altair) for timelines, rankings, and drill-downs  
- **Geospatial maps** (launch sites, country contributions) with GeoPandas/Folium  
- **Network graphs** (agency–mission–partner relationships)  
- **CLI utilities** to filter, aggregate, and export charts/tables  
- **Makefile / pip-tools** for reproducible environments and runs

---

## Data Sources

> Use any open datasets you have permissions for. Common starting points include:
- Historical launch logs from public encyclopedic datasets
- National space agencies’ open data portals
- International statistics (e.g., country-level space indicators)
- Launch site coordinates (open geodata)
- Company/agency reference lists

*(You can update `data/sources.md` with exact links and licensing for your chosen datasets.)*

---

## Requirements

- Python 3.9+  
- Recommended libraries:
  - Core: `pandas`, `numpy`, `python-dateutil`
  - Viz: `matplotlib`, `plotly`, `altair`, `folium`, `graphviz` (via `pygraphviz` or `graphviz` binaries)
  - Geo: `geopandas`, `shapely`
  - Utilities: `typer` (CLI), `rich` (pretty console), `pyyaml`
  - Dev: `jupyter`, `pre-commit`, `black`, `isort`

Install (base set):
```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/space-race-analytics.git
   cd space-race-analytics
   ```
2. Create & activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Quick Start

Run the end-to-end pipeline (ingest → clean → build charts → open dashboard):
```bash
make all
# or
python -m src.cli ingest --from data/raw
python -m src.cli clean
python -m src.cli build-charts --out reports/figures
python -m src.cli serve-dashboard
```

Open the dashboard at:
```
http://127.0.0.1:8050/
```

---

## Usage

### 1) Ingest & Clean
```bash
python -m src.cli ingest --from data/raw --format csv
python -m src.cli clean --country-map data/reference/country_map.csv --agency-map data/reference/agency_map.csv
```

### 2) Generate Figures
```bash
python -m src.cli build-charts --out reports/figures --interactive
```

### 3) Run Notebooks
```bash
jupyter lab  # open notebooks in notebooks/
```

### 4) Export Subsets
```bash
python -m src.cli export --query "year>=1957 and country in ['USA','USSR','Russia','China','Europe']" \
  --columns "year,country,agency,vehicle,payload_kg,orbit" \
  --out data/processed/space_race_subset.csv
```

---

## Project Structure

```
space-race-analytics/
├── data/
│   ├── raw/                 # Original datasets (read-only)
│   ├── interim/             # Staged data after initial cleaning
│   ├── processed/           # Final analysis-ready tables
│   └── reference/           # Mapping files (country/agency aliases, sites)
├── notebooks/
│   ├── 01_eda_overview.ipynb
│   ├── 02_launch_trends.ipynb
│   ├── 03_payload_orbits.ipynb
│   └── 04_networks_and_sites.ipynb
├── reports/
│   ├── figures/             # Exported charts (png/html)
│   └── dashboard/           # Built dashboard assets
├── src/
│   ├── cli.py               # Typer CLI entrypoint
│   ├── etl/
│   │   ├── ingest.py        # Load CSV/JSON → parquet
│   │   ├── clean.py         # Standardise fields, fix dates/aliases
│   │   └── validate.py      # Schema & logic checks
│   ├── features/
│   │   ├── derive_metrics.py# KPIs, rolling stats
│   │   └── geography.py     # Geospatial joins, site mapping
│   ├── viz/
│   │   ├── charts.py        # Timelines, bars, small multiples
│   │   ├── maps.py          # Choropleths, dot maps
│   │   └── networks.py      # Collaboration graphs
│   └── dashboard/
│       └── app.py           # Dash/Streamlit app
├── requirements.txt
├── Makefile
└── README.md
```

---

## Data Model

**Table: `launches` (analysis-ready)**  
- `launch_id` (string, unique)  
- `date` (date)  
- `year` (int)  
- `country` (string, ISO or friendly name)  
- `agency` (string, normalised)  
- `vehicle` (string)  
- `site_name` (string)  
- `site_lat`, `site_lon` (float)  
- `mission_type` (enum: comms, earth_obs, crewed, science, nav, test, etc.)  
- `orbit` (enum: LEO/MEO/GEO/HEO/Suborbital/Interplanetary)  
- `payload_name` (string)  
- `payload_kg` (float, nullable)  
- `outcome` (enum: success/partial/failure)  

**Table: `entities` (reference)**  
- `name` (agency/company), `country`, `founded_year`, `type` (gov/commercial)

---

## Visualisations

- **Launches Over Time**: yearly line chart per country/agency with moving average  
- **Success Rate by Decade**: stacked bars or heatmap (vehicle × decade)  
- **Payload Capacity Trend**: median/quantile payload mass over time  
- **Orbit Distribution**: sunburst or stacked bars (country → orbit)  
- **Milestone Timeline**: annotated timeline of landmark events  
- **Geospatial Map**: choropleth of launches by country; dot map of launch sites  
- **Collaboration Network**: force-directed graph (agency ↔ partner projects)

All interactive charts exportable to HTML in `reports/figures/`.

---

## Reproducibility

- **Versioned data**: keep `data/raw/` read-only; all transforms are scripted.  
- **Deterministic runs**: set random seeds where applicable.  
- **Environment**:
  ```bash
  pip freeze > requirements-lock.txt
  ```
- **Pre-commit hooks**:
  ```bash
  pre-commit install
  ```

---

## Minimal Code Snippet

```python
# src/viz/charts.py (example)
import pandas as pd
import plotly.express as px

def launches_over_time(df: pd.DataFrame, by="country"):
    ts = (
        df.groupby(["year", by], as_index=False)
          .size()
          .rename(columns={"size": "launches"})
    )
    fig = px.line(ts, x="year", y="launches", color=by,
                  title=f"Launches per Year by {by.title()}")
    return fig
```

---

## Contributing

Contributions are welcome!  
1) Fork the repo • 2) Create a branch (`feat/trend-map`) • 3) Commit & push • 4) Open a PR  
Please include:
- Clear description & screenshots of new visuals
- Tests for ETL/validation logic (if modified)
- Updates to `data/sources.md` when adding datasets

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
