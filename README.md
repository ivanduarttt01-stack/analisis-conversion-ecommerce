# Análisis de abandono de carrito y conversión en e-commerce

## Contexto del caso

**Lima & Lino** es una tienda online ficticia de decoración y productos para el hogar. A comienzos de 2025, el equipo comercial notó que las visitas al sitio venían creciendo, pero las ventas no acompañaban el mismo ritmo. También aumentaron las consultas al canal de atención sobre costos de envío y promociones.

La gerencia pidió al equipo de Datos revisar el recorrido de compra: desde que una persona agrega un producto al carrito hasta que finaliza el pago. El objetivo no era solamente medir una tasa general de conversión, sino encontrar en qué parte del proceso se perdían oportunidades y qué acciones concretas podían probarse.

Este repositorio documenta ese análisis de punta a punta. Los datos son sintéticos y se generaron exclusivamente para fines de portafolio, pero las preguntas, métricas y decisiones propuestas responden a una situación habitual de comercio electrónico.

## Pedido del negocio

El equipo de Marketing y E-commerce solicitó responder estas preguntas:

- ¿Cuál es la tasa de conversión desde carrito hasta compra?
- ¿En qué dispositivo, canal de adquisición y categoría se concentra el abandono?
- ¿El costo de envío y el tiempo de carga se asocian con una menor conversión?
- ¿Qué experimentos deberían priorizarse durante el próximo mes?

## Objetivo

Analizar 25.000 sesiones con carrito para detectar fricciones en el proceso de compra y proponer acciones que ayuden a aumentar las ventas sin depender únicamente de invertir más en publicidad.

## Trabajo realizado

1. Se generó y documentó una base sintética de sesiones de compra.
2. Se validó la calidad de los datos: identificadores únicos, fechas válidas y coherencia entre las etapas del embudo.
3. Se construyó un embudo de conversión: carrito → checkout → compra.
4. Se segmentaron resultados por dispositivo, canal, categoría, costo de envío y tiempo de carga.
5. Se estimó el impacto potencial de las acciones recomendadas usando el comportamiento observado.

## Hallazgos principales

- El abandono es más alto en **móvil**, principalmente entre el carrito y el inicio del checkout.
- Las sesiones que muestran un costo de envío superior a un umbral relativo al valor del carrito convierten menos.
- El tráfico proveniente de campañas pagadas genera volumen, pero presenta menor conversión que email y tráfico directo.
- Cuando la página tarda más de tres segundos en cargar, el avance al checkout cae de forma visible.
- Decoración y textiles concentran el mayor volumen de carritos abandonados, por lo que son categorías adecuadas para priorizar pruebas.

## Recomendaciones

| Prioridad | Acción propuesta | Métrica a seguir |
|---|---|---|
| Alta | Mostrar la estimación de envío antes de iniciar checkout, especialmente en móvil. | Conversión carrito → checkout |
| Alta | Optimizar la carga de la página de carrito en móvil. | Tiempo de carga y abandono |
| Media | Probar envío gratis a partir de un monto mínimo en categorías seleccionadas. | Conversión y margen por pedido |
| Media | Activar un recordatorio de carrito abandonado por email. | Recuperación de carritos |

Estas recomendaciones son hipótesis de mejora; antes de escalarlas, deberían validarse con pruebas A/B y métricas de margen, no solo de conversión.

## Herramientas utilizadas

- **Python:** generación, limpieza y análisis de datos.
- **Pandas:** transformación y cálculo de métricas.
- **Matplotlib:** gráficos del embudo y segmentación.
- **SQL (PostgreSQL):** consultas de embudo y desempeño por canal.
- **Git/GitHub:** documentación y control de versiones.

## Estructura del repositorio

```text
├── data/
│   ├── raw/                  # Base sintética generada por script
│   └── data_dictionary.md
├── docs/
│   └── informe_ejecutivo.md
├── sql/
│   ├── 01_create_table.sql
│   └── 02_funnel_analysis.sql
├── src/
│   ├── generate_data.py
│   └── analysis.py
├── outputs/                  # Tablas y gráficos creados al ejecutar el análisis
├── requirements.txt
└── README.md
```

## Cómo reproducirlo

Esta sección es opcional para quien visite el repositorio; sirve para mostrar que el análisis es reproducible.

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/analysis.py
```

## Cómo describirlo en un CV

**Proyecto de portafolio — Analista de Datos, E-commerce (caso simulado)**  
Analicé 25.000 sesiones de compra con Python y SQL para identificar fricciones en el embudo de conversión. Detecté oportunidades en la experiencia móvil, transparencia de costos de envío y recuperación de carritos, y propuse experimentos medibles para mejorar conversiones.

## Autor

**Iván Duarte** — Proyecto de portafolio para posiciones de Analista de Datos.
