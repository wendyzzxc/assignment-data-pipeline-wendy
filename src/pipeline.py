from __future__ import annotations
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_data(filepath: str) -> pd.DataFrame:
  df = pd.read_csv(filepath)

  print("5 baris pertama dataset:\n", df.head())
  print(f"\nJumlah kolom dataset: {len(df.columns)} kolom")
  print(f"\nJumlah baris dataset: {len(df)} baris")
  print("\nNama Setiap kolom dataset:\n", df.columns)
  print("\nTipe data setiap kolom dataset:\n", df.dtypes)
  print("\nJumlah missing values pada setiap kolom dataset:\n", df.isna().sum())
  print(f"\nJumlah duplicates dataset: {df.duplicated().sum()} baris")
  print("\nNilai unik pada kolom:", df["make"].value_counts())
  print("\nNilai unik pada kolom:", df["body-style"].value_counts())
  print("\nNilai unik pada kolom:", df["fuel-system"].value_counts())
  print("\nNilai unik pada kolom:", df["drive-wheels"].value_counts())

  return df



def clean_data(df: pd.DataFrame) -> pd.DataFrame:
  duplicate = df.duplicated().sum()

  print(f"Jumlah data sebelum cleaning: {len(df)} baris")
  print(f"Jumlah missing value sebelum cleaning: {df.isna().sum().sum()}")

  # Missing value
  df["transaction_date"] = df["transaction_date"].ffill()
  df["make"] = df["make"].fillna("")
  df["num-of-doors"] = df["num-of-doors"].fillna(df["num-of-doors"].mode()[0])
  df["stroke"] = df["stroke"].fillna(df["stroke"].mean())
  df["horsepower"] = df["horsepower"].fillna(df["horsepower"].mean())
  df["price"] = df["price"].fillna(df["price"].median())
  df["horsepower-binned"] = df["horsepower-binned"].fillna("")

  # duplicate columns
  df = df.drop_duplicates(keep="first")

  # format
  df["make"] = df["make"].str.lower().str.strip()
  df["body-style"] = df["body-style"].str.lower().str.strip()
  df["drive-wheels"] = df["drive-wheels"].str.lower().str.strip()
  df["fuel-system"] = df["fuel-system"].str.lower().str.strip()
  df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce", format="mixed")

  # tipe data
  df["horsepower"] = df["horsepower"].astype("int64")
  df["compression-ratio"] = df["compression-ratio"].astype("int64")
  df["peak-rpm"] = df["peak-rpm"].astype("int64")
  df["price"] = df["price"].astype("int64")

  print(f"Jumlah data sesudah cleaning: {len(df)} baris")
  print(f"Jumlah missing value sesudah cleaning: {df.isna().sum().sum()}")
  print(f"Jumlah baris duplikasi yang dihapus {duplicate} baris")
  print(f"Kolom yang mengalami perubahan: ['transaction_date', 'make', 'num-of-doors', 'stroke', 'horsepower', 'price', 'horsepower-binned, 'body-style', 'drive-wheels', 'fuel-system', 'compression-ratio', 'peak-rpm']")

  return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
  # MinMax scaling
  scaler = MinMaxScaler()
  df[["price_norm"]] = scaler.fit_transform(df[["price"]])  

  # One-hot encoding
  df = pd.get_dummies(df, columns=["horsepower-binned"], prefix="horsepower_binned")

  print(f"[transform] {df.shape[1]} kolom setelah transformasi")
  return df

def save_data(df: pd.DataFrame, filepath: str) -> None:
    df.to_csv(filepath, index=False)
    print(f"[save]  {filepath}")


def main() -> None:
    df = load_data("../data/raw/automobileEDA_dirty_training.csv")
    df = clean_data(df)
    df = transform_data(df)
    save_data(df, "../data/processed/automobileEDA_processed.csv")
    print("Pipeline selesai ✓")


if __name__ == "__main__":
    main()
