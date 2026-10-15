CREATE TABLE sesiones_carrito (
    sesion_id VARCHAR(20) PRIMARY KEY,
    fecha DATE NOT NULL,
    dispositivo VARCHAR(20) NOT NULL,
    canal VARCHAR(30) NOT NULL,
    categoria_principal VARCHAR(50) NOT NULL,
    valor_carrito_usd NUMERIC(10,2) CHECK (valor_carrito_usd > 0),
    costo_envio_usd NUMERIC(10,2) CHECK (costo_envio_usd >= 0),
    tiempo_carga_seg NUMERIC(5,2) CHECK (tiempo_carga_seg > 0),
    inicio_checkout BOOLEAN NOT NULL,
    compra_completada BOOLEAN NOT NULL,
    valor_compra_usd NUMERIC(10,2) CHECK (valor_compra_usd >= 0),
    CHECK (NOT compra_completada OR inicio_checkout)
);

-- PostgreSQL: \copy sesiones_carrito FROM 'data/raw/sesiones_carrito_2025.csv' CSV HEADER;
