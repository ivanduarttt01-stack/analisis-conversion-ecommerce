"""Crea sesiones sintéticas para el caso de análisis de e-commerce."""
from pathlib import Path
from datetime import date, timedelta
import csv
import random

random.seed(2025)
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "sesiones_carrito_2025.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

dispositivos = [("Móvil", 0.62), ("Desktop", 0.31), ("Tablet", 0.07)]
canales = [("Orgánico", 0.28), ("Pago", 0.30), ("Email", 0.16), ("Directo", 0.15), ("Redes Sociales", 0.11)]
categorias = [("Decoración", 0.30), ("Textiles", 0.25), ("Cocina", 0.22), ("Iluminación", 0.13), ("Muebles", 0.10)]
inicio = date(2025, 1, 1)

with OUT.open("w", newline="", encoding="utf-8") as f:
    columns = ["sesion_id", "fecha", "dispositivo", "canal", "categoria_principal", "valor_carrito_usd", "costo_envio_usd", "tiempo_carga_seg", "inicio_checkout", "compra_completada", "valor_compra_usd"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for n in range(1, 25001):
        dispositivo = random.choices([x[0] for x in dispositivos], weights=[x[1] for x in dispositivos])[0]
        canal = random.choices([x[0] for x in canales], weights=[x[1] for x in canales])[0]
        categoria = random.choices([x[0] for x in categorias], weights=[x[1] for x in categorias])[0]
        valor = round(max(12, random.lognormvariate(4.15, 0.48)), 2)
        envio = round(max(0, random.gauss(7.5 if valor < 75 else 4.5, 2.3)), 2)
        carga = round(max(0.8, random.gauss(3.3 if dispositivo == "Móvil" else 2.1, 0.9)), 2)
        prob_checkout = 0.69
        if dispositivo == "Móvil": prob_checkout -= 0.09
        if carga > 3: prob_checkout -= 0.12
        if envio / valor > 0.12: prob_checkout -= 0.15
        if canal == "Email": prob_checkout += 0.07
        checkout = random.random() < prob_checkout
        prob_compra = 0.74
        if dispositivo == "Móvil": prob_compra -= 0.06
        if carga > 3: prob_compra -= 0.06
        if canal == "Pago": prob_compra -= 0.04
        compra = checkout and random.random() < prob_compra
        writer.writerow({"sesion_id": f"LL-{n:05d}", "fecha": (inicio + timedelta(days=random.randrange(180))).isoformat(), "dispositivo": dispositivo, "canal": canal, "categoria_principal": categoria, "valor_carrito_usd": valor, "costo_envio_usd": envio, "tiempo_carga_seg": carga, "inicio_checkout": checkout, "compra_completada": compra, "valor_compra_usd": valor if compra else 0})

print(f"Datos creados: {OUT}")
