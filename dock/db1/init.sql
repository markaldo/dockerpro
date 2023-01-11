CREATE TABLE IF NOT EXISTS supply(
   id SERIAL,
   batch character varying(50),
   price character varying(50),
   date date,
   CONSTRAINT kit_pkey PRIMARY KEY (id)
);
