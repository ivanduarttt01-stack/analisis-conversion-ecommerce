"""Calcula el embudo y guarda tablas y gráficos del caso."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "data" / "raw" / "sesiones_carrito_2025.csv", parse_dates=["fecha"])

assert df["sesion_id"].is_unique
assert df.notna().all().all()
assert not (df["compra_completada"] & ~df["inicio_checkout"]).any()

embudo = pd.DataFrame({"etapa": ["Carritos", "Inicio de checkout", "Compras"], "sesiones": [len(df), df.inicio_checkout.sum(), df.compra_completada.sum()]})
embudo["conversion_sobre_carrito"] = (embudo["sesiones"] / len(df) * 100).round(1)
embudo.to_csv(OUT / "embudo_conversion.csv", index=False)

segmentos = (df.groupby(["dispositivo", "canal"], as_index=False)
    .agg(sesiones=("sesion_id", "count"), pct_checkout=("inicio_checkout", "mean"), pct_conversion=("compra_completada", "mean"), ingreso=("valor_compra_usd", "sum")))
segmentos[["pct_checkout", "pct_conversion"]] = (segmentos[["pct_checkout", "pct_conversion"]] * 100).round(1)
segmentos.to_csv(OUT / "conversion_por_segmento.csv", index=False)

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(embudo["etapa"], embudo["sesiones"], color=["#457B9D", "#1D3557", "#E76F51"])
ax.set(title="Embudo de conversión", ylabel="Cantidad de sesiones")
for i, val in enumerate(embudo["conversion_sobre_carrito"]): ax.text(i, embudo["sesiones"].iloc[i] + 300, f"{val}%", ha="center")
fig.tight_layout(); fig.savefig(OUT / "embudo_conversion.png", dpi=160); plt.close(fig)

por_dispositivo = df.groupby("dispositivo")["compra_completada"].mean().mul(100).sort_values()
fig, ax = plt.subplots(figsize=(7, 4))
por_dispositivo.plot(kind="bar", ax=ax, color="#2A9D8F")
ax.set(title="Conversión por dispositivo", xlabel="", ylabel="Compras / carritos (%)", ylim=(0, 60)); ax.tick_params(axis="x", rotation=0)
fig.tight_layout(); fig.savefig(OUT / "conversion_dispositivo.png", dpi=160); plt.close(fig)
print("Análisis terminado. Revisá la carpeta outputs/.")
