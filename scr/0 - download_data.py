from pathlib import Path
import pandas as pd
import subprocess
import sys

pd.set_option("display.max_columns", None)

try:
    import kagglehub
    from kagglehub import KaggleDatasetAdapter
except ImportError:
    print("🔄 Instalando kagglehub automaticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kagglehub[pandas-datasets]", "pyarrow"])
    import kagglehub
    from kagglehub import KaggleDatasetAdapter

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "BlastChar/telco-customer-churn",
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

data_path = Path(__file__).resolve().parents[1] / "data"
data_path.mkdir(parents=True, exist_ok=True)

df.to_parquet(data_path / "dados_banco.parquet", index=False)
df.to_csv(data_path / "dados_banco.csv", index=False)

print("✅ Dataset salvo em:", data_path / "dados_banco.parquet")