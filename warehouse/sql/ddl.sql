CREATE SCHEMA IF NOT EXISTS crypto;

CREATE TABLE crypto.stg_crypto_prices (

    symbol VARCHAR(20),

    price DOUBLE PRECISION,

    timestamp TIMESTAMP,

    year INT,
    month INT,
    day INT
);


CREATE TABLE crypto.fact_crypto_prices (

    symbol VARCHAR(20),

    price DOUBLE PRECISION,

    timestamp TIMESTAMP,

    year INT,
    month INT,
    day INT

)
SORTKEY(timestamp);

CREATE TABLE crypto.etl_metadata (

    partition_path VARCHAR(500),

    loaded_at TIMESTAMP DEFAULT GETDATE()
);
