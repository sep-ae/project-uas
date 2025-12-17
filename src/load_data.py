import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo

# =========================
# LOAD DATASET
# =========================
dow = fetch_ucirepo(id=312)
X = dow.data.features
y = dow.data.targets
df = pd.concat([X, y], axis=1)

# =========================
# FIX DATA TYPES
# =========================
num_cols_obj = [
    "open", "high", "low", "close",
    "next_weeks_open", "next_weeks_close"
]

for col in num_cols_obj:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

# =========================
# 4.2 DESKRIPSI FITUR
# =========================
feature_desc = {
    "quarter": "Kuartal dalam satu tahun (1–4)",
    "stock": "Kode saham Dow Jones",
    "date": "Tanggal akhir minggu",
    "open": "Harga pembukaan minggu",
    "high": "Harga tertinggi minggu",
    "low": "Harga terendah minggu",
    "close": "Harga penutupan minggu",
    "volume": "Volume transaksi saham",
    "percent_change_price": "Persentase perubahan harga minggu berjalan",
    "percent_change_volume_over_last_wk": "Perubahan volume dibanding minggu sebelumnya",
    "previous_weeks_volume": "Volume transaksi minggu sebelumnya",
    "next_weeks_open": "Harga pembukaan minggu berikutnya",
    "next_weeks_close": "Harga penutupan minggu berikutnya",
    "days_to_next_dividend": "Jumlah hari menuju dividen berikutnya",
    "percent_return_next_dividend": "Persentase return dividen",
    "percent_change_next_weeks_price": "Persentase perubahan harga minggu berikutnya (TARGET)"
}

desc_table = []
for col in df.columns:
    desc_table.app_
