CREATE TABLE customer ( id INTEGER, 
                        name VARCHAR(500), 
                        jdate DATE, 
                        address TEXT, 
                        email VARCHAR(500));
 
CREATE TABLE invoice  ( cid INTEGER REFERENCES customer(id),
                        id INTEGER PRIMARY KEY, 
                        date DATE, 
                        particulars text, 
                        amount NUMERIC);
 
INSERT INTO invoice VALUES (3, 1, '2020-Feb-01', 'Machine learning', 450);
INSERT INTO customer(id, name, jdate, address, email) VALUES (1, 'John and sons', '2020-Feb-01', '5th Street', 'john@johnandsons.com');
INSERT INTO customer(id, name, jdate, address, email) VALUES (3, 'Batman', '2020-Jan-01', '5th Street, Gotham', 'bruce@wayne.net');
INSERT INTO customer(id, name, jdate, address, email) VALUES (2, 'Superman', '2015-July-04', '5th Street, Metropolis', 'clark@dailyplanet.com');
 
ALTER TABLE customer ADD PRIMARY KEY (id);

ALTER TABLE customer ADD NOT NULL (id);
 
SELECT * FROM customer where id=2;

DROP DATABASE invoice;

SELECT * FROM customer;
SELECT * FROM invoice_customer;
SELECT * FROM invoice_invoice;
