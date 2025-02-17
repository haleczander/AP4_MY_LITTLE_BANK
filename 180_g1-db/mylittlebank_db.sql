DROP DATABASE IF EXISTS mylittlebank;
CREATE DATABASE mylittlebank;
CONNECT TO mylittlebank;
DROP TABLE IF EXISTS account CASCADE;
DROP TABLE IF EXISTS transaction CASCADE;
DROP TABLE IF EXISTS exchange_rate CASCADE;
DROP TABLE IF EXISTS currency CASCADE;
DROP TABLE IF EXISTS transaction_type CASCADE;

CREATE TABLE currency (
    code VARCHAR(3) PRIMARY KEY
);


CREATE TABLE account (
    account_number SERIAL PRIMARY KEY,
    currency VARCHAR(3) REFERENCES currency(code) NOT NULL,
    balance DECIMAL(15,2) NOT NULL
);

insert into currency( code ) VALUES ('USD'), ('EUR'), ('JPY'), ('GBP'), ('AUD'), ('CAD'), ('CHF'), ('CNY'), ('SEK'), ('NZD');

CREATE TABLE exchange_rate (
    exchange_rate_id SERIAL PRIMARY KEY,
    from_currency VARCHAR(3) references currency(code) NOT NULL,
    to_currency VARCHAR(3) references currency(code) NOT NULL,
    rate FLOAT NOT NULL
);

CREATE TABLE transaction_type (
    id SERIAL PRIMARY KEY ,
    name VARCHAR(20) NOT NULL
);

INSERT INTO transaction_type (name) VALUES ('CARD'), ('CHECK'), ('TRANSFER');

CREATE TABLE transaction (
    transaction_id SERIAL PRIMARY KEY,
    type int REFERENCES transaction_type(id) NOT NULL,
    source_account INT references account(account_number) NOT NULL,
    amount FLOAT NOT NULL,
    currency VARCHAR(3) references currency(code) NOT NULL,
    label VARCHAR(255),
    dest_account INT references account(account_number),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


