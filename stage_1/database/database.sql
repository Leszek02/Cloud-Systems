CREATE TABLE IF NOT EXISTS tesla_insider_trading (
    id SERIAL PRIMARY KEY,
    insider_trading varchar(100),
    relationship varchar(100),
    date date, -- TODO: wrong datatype here
    transaction varchar(20),
    cost decimal(6,2),
    shares varchar(20),
    value varchar(20),
    shares_total varchar(20),
    sec_form_4 varchar(30)
);

COPY tesla_insider_trading 
    (insider_trading, relationship, date, transaction, cost, shares, value, shares_total, sec_form_4)
    FROM '/TSLA.csv'
    DELIMITER ','
    CSV HEADER;
