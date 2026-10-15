-- Embudo por dispositivo y canal
SELECT
    dispositivo,
    canal,
    COUNT(*) AS carritos,
    ROUND(100.0 * AVG(inicio_checkout::int), 1) AS pct_inicio_checkout,
    ROUND(100.0 * AVG(compra_completada::int), 1) AS pct_conversion,
    ROUND(AVG(valor_compra_usd) FILTER (WHERE compra_completada), 2) AS ticket_promedio
FROM sesiones_carrito
GROUP BY 1, 2
ORDER BY pct_conversion;

-- Impacto de envío y rendimiento
SELECT
    CASE WHEN costo_envio_usd / valor_carrito_usd > 0.12 THEN 'Envío alto' ELSE 'Envío bajo/medio' END AS nivel_envio,
    CASE WHEN tiempo_carga_seg > 3 THEN 'Más de 3 segundos' ELSE 'Hasta 3 segundos' END AS rendimiento,
    COUNT(*) AS sesiones,
    ROUND(100.0 * AVG(compra_completada::int), 1) AS pct_conversion
FROM sesiones_carrito
GROUP BY 1, 2
ORDER BY pct_conversion;
