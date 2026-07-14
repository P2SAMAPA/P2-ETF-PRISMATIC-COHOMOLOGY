# Prismatic Cohomology for ETFs

Applies the latest development in p-adic geometry (Bhatt-Scholze) to ETF price structures. Unifies étale, crystalline, and de Rham cohomologies, providing a universal framework for analyzing discrete price structures across different "characteristics." The per‑ETF score is the prismatic cohomology rank.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- Unifies de Rham, crystalline, and étale cohomologies
- Prismatic embedding via moments, p-adic valuations, and topological features
- Score = prismatic cohomology rank (higher = more universal structure)
- Two‑tab Streamlit dashboard (auto best, manual)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-prismatic-cohomology-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python train.py` (fast)
4. Launch dashboard: `streamlit run streamlit_app.py`

## Interpretation

- High prismatic rank → more universal cohomological structure.
- Low prismatic rank → simpler structure.

## Requirements

See `requirements.txt`.
