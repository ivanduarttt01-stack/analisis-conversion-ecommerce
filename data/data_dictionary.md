# Diccionario de datos

| Campo | Descripción |
|---|---|
| `sesion_id` | Identificador único de la sesión. |
| `fecha` | Fecha de la sesión. |
| `dispositivo` | Móvil, Desktop o Tablet. |
| `canal` | Origen de adquisición: Orgánico, Pago, Email, Directo o Redes Sociales. |
| `categoria_principal` | Categoría del producto agregado al carrito. |
| `valor_carrito_usd` | Valor total del carrito en USD. |
| `costo_envio_usd` | Costo estimado de envío mostrado. |
| `tiempo_carga_seg` | Tiempo de carga de la página de carrito. |
| `inicio_checkout` | Indica si la sesión inició checkout. |
| `compra_completada` | Indica si la sesión terminó en compra. |
| `valor_compra_usd` | Valor final de compra; cero si no se completó. |

## Reglas de calidad

- Una compra completada siempre implica inicio de checkout.
- El valor de compra es cero cuando no hay compra.
- No existen identificadores duplicados ni valores nulos.
