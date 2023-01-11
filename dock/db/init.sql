CREATE TABLE kit(
   id SERIAL,
   name character varying(50),
   CONSTRAINT kit_pkey PRIMARY KEY (id)
);

INSERT INTO kit(name)
VALUES 
('Gun'),
('Hickboots'),
('Jacket'),
('Demin'),
('Knife'),
('Tin'),
('Woolen hat'),
('Satchel');