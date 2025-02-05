CREATE DATABASE mylittlebank;

CREATE TABLE Account (
    account_number BIGINT,
    currency VARCHAR(3),
    balance DECIMAL(15,2) NOT NULL,
    PRIMARY KEY (account_number, currency),
    FOREIGN KEY (currency) REFERENCES Currency(code)
);

CREATE TABLE Currency (
    code VARCHAR(3) PRIMARY KEY,
    is_allowed BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE ExchangeRate (
    from_currency VARCHAR(3),
    to_currency VARCHAR(3),
    rate DECIMAL(10,6) NOT NULL,
    PRIMARY KEY (from_currency, to_currency),
    FOREIGN KEY (from_currency) REFERENCES Currency(code),
    FOREIGN KEY (to_currency) REFERENCES Currency(code)
);

CREATE TABLE Transaction (
    source_account BIGINT,
    source_currency VARCHAR(3),
    dest_account BIGINT,
    dest_currency VARCHAR(3),
    amount DECIMAL(15,2) NOT NULL,
    type ENUM('CARD', 'CHECK', 'TRANSFER') NOT NULL,
    label VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (source_account, source_currency, timestamp),
    FOREIGN KEY (source_account, source_currency) REFERENCES Account(account_number, currency),
    FOREIGN KEY (dest_account, dest_currency) REFERENCES Account(account_number, currency)
);


