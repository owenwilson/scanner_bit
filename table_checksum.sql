CREATE TABLE IF NOT EXISTS check_sum (
    domain_subdomain serial PRIMARY KEY,
    checksum VARCHAR (150) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
)
