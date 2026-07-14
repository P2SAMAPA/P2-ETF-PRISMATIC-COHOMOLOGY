import os

HF_TOKEN = os.environ.get("HF_TOKEN", "")
DATA_REPO = "P2SAMAPA/fi-etf-macro-signal-master-data"
OUTPUT_REPO = "P2SAMAPA/p2-etf-prismatic-cohomology-results"

WINDOWS = [63, 252, 504, 1008, 2016, 4032, 4536]

UNIVERSES = {
    "FI_COMMODITIES": ["TLT", "VCIT", "LQD", "HYG", "VNQ", "GLD", "SLV"],
    "EQUITY_SECTORS": [
        "SPY", "QQQ", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "SMH", "SOXX", "XLB",
        "XLP", "XLU", "GDX", "XME", "IWF", "XSD", "XBI", "IWM", "IWD", "IWO"
    ],
    "COMBINED": [
        "TLT", "VCIT", "LQD", "HYG", "VNQ", "GLD", "SLV",
        "SPY", "QQQ", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "SMH", "SOXX", "XLB",
        "XLP", "XLU", "GDX", "XME", "IWF", "XSD", "XBI", "IWM", "IWD", "IWO"
    ]
}

# All available macro variables
MACRO_VARS = [
    "VIX", "DXY", "T10Y2Y", "TBILL_3M",
    "DGS1MO", "DGS3MO", "DGS6MO", "DGS1", "DGS2", "DGS5", "DGS7",
    "DGS10", "DGS20", "DGS30"
]

# Prismatic cohomology parameters
P_ADIC_BASE = 2              # p-adic base (2, 3, 5, etc.)
PRISMATIC_DIM = 15           # dimension of prismatic representation
UNIFICATION_LEVELS = 5       # levels for unifying different cohomologies
TOP_N = 3
