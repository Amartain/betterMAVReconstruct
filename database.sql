--Acount tábla:

CREATE TABLE felhasznalo (
	nev varchar2(20) NOT NULL,
	jelszo varchar2(30) NOT NULL,
	emai varchar2(20) NOT NULL,
	CONSTRAINT nev_pk PRIMARY KEY (nev)
);

--Menetrend tábla:

CREATE TABLE menetrend (
	allomasNev varchar2(30) NOT NULL,
	honnan varchar2(20) NOT NULL,
	hova varchar2(20) NOT NULL,
	tav integer NOT NULL,
	erkezes DATE NOT NULL,
	tavozas DATE NOT NULL,
	peron varchar2(5) NOT NULL,
	CONSTRAINT allomasNev_pk PRIMARY KEY (allomasNev)
	FOREIGN KEY (honnan, hova) REFERENCES varosok(nev)
);

--Városok tábla:

CREATE TABLE varosok (
	irsz number(5) NOT NULL,
	nev varchar2(20) NOT NULL,
	varMegye varchar2(20) NOT NULL,
	CONSTRAINT irsz_pk PRIMARY KEY (irsz)
);

--Állomások tábla:

--Vasút vonal tábla:

--Jegykategória tábla:

CREATE TABLE jegy_kategoria(
	azon varchar2(25) NOT NULL,
	nev varchar2(50) NOT NULL,
	kedvezmeny integer,
	arak text,
	CONSTRAINT azon_pk PRIMARY KEY (azon)
);


--Jegyvásárlás tábla:

CREATE TABLE jegyek (
	id number NOT NULL,
	honnan varchar2(20) NOT NULL,
	hova varchar2(20) NOT NULL,
	tav integer NOT NULL,
	ar integer NOT NULL,
	tipus varchar2(25) NOT NULL,
	ervenyesseg_kezdete timestamp NOT NULL,
	CONSTRAINT id_pk PRIMARY KEY (id),
	CONSTRAINT fk_jegyek FOREIGN KEY (tipus) REFERENCES jegy_kategoria(azon)
	CONSTRAINT fk_jegyek FOREIGN KEY (honnan) REFERENCES menetrend(honnan)
	CONSTRAINT fk_jegyek FOREIGN KEY (hova) REFERENCES menetrend(hova)
	ON DELETE RESTRICT
	ON UPDATE RESTRICT
);

CREATE SEQUENCE jegyek_ai
START WITH 1
INCREMENT BY 1
NOMAXVALUE;

CREATE OR REPLACE TRIGGER jegyek_ai_trigger
BEFORE INSERT ON jegyek
FOR EACH ROW
BEGIN
	SELECT jegyek_ai.NEXTVAL INTO :NEW.id FROM DUAL;
END;


--Adatok felvitele:

INSERT INTO jegy_kategoria VALUES ('teljes', 'teljesárú', 0, '10:250; 20:370; 30:560; 40:745; 51:930');
INSERT INTO jegy_kategoria VALUES ('diák', 'diákjegy', 50, '10:125; 20:185; 30:280; 40:375; 51:465');
INSERT INTO jegy_kategoria VALUES ('közalkalmazotti', 'közalkalmazotti jegy', 50, '10:125; 20:185; 30:280; 40:375; 51:465');
INSERT INTO jegy_kategoria VALUES ('hétvégi', 'hétvégi jegy', 33, '10:170; 20:250; 30:375; 40:500; 51:625');
INSERT INTO jegy_kategoria VALUES ('családi', 'családi jegy', 33, '10:170; 20:250; 30:375; 40:500; 51:625');

INSERT INTO jegyek (honnan, hova, tav, ar, tipus, ervenyesseg_kezdete) VALUES ('Szeged', 'Szatymaz', 16, 370, 'teljes', TIMESTAMP '2024-03-22 08:00:00');
INSERT INTO jegyek (honnan, hova, tav, ar, tipus, ervenyesseg_kezdete) VALUES ('Szeged', 'Szatymaz', 16, 370, 'teljes', TIMESTAMP '2024-03-22 09:00:00');
INSERT INTO jegyek (honnan, hova, tav, ar, tipus, ervenyesseg_kezdete) VALUES ('Szeged', 'Szatymaz', 16, 185, 'diak', TIMESTAMP '2024-03-22 09:00:00');
INSERT INTO jegyek (honnan, hova, tav, ar, tipus, ervenyesseg_kezdete) VALUES ('Szeged', 'Szatymaz', 16, 250, 'csaladi', TIMESTAMP '2024-03-22 08:00:00');
INSERT INTO jegyek (honnan, hova, tav, ar, tipus, ervenyesseg_kezdete) VALUES ('Kistelek', 'Kiskunfélegyháza', 29, 375, 'hetvegi', TIMESTAMP '2024-03-23 00:00:00');

INSERT INTO varosok (irsz, nev, varMegye) VALUES (6720, 'Szeged', 'Csongrád-Csanád');
INSERT INTO varosok (irsz, nev, varMegye) VALUES (6800, 'Hódmezővásárhely', 'Csongrád-Csanád');
INSERT INTO varosok (irsz, nev, varMegye) VALUES (6900, 'Makó', 'Csongrád-Csanád');
INSERT INTO varosok (irsz, nev, varMegye) VALUES (6821, 'Székkutas', 'Csongrád-Csanád');
INSERT INTO varosok (irsz, nev, varMegye) VALUES (6600, 'Szentes', 'Csongrád-Csanád');

INSERT INTO felhasznalo (nev, jelszo, email) VALUES ('PumPal', 'PumPal123', 'pumpal@test.com');
INSERT INTO felhasznalo (nev, jelszo, email) VALUES ('JohnDoe', 'JohnDoe123', 'johndoe@test.com');
INSERT INTO felhasznalo (nev, jelszo, email) VALUES ('JaneDoe', 'JaneDoe123', 'janedoe@test.com');
INSERT INTO felhasznalo (nev, jelszo, email) VALUES ('CsetElek', 'CsetElek123', 'csetelek@test.com'));
INSERT INTO felhasznalo (nev, jelszo, email) VALUES ('DizElek', 'DizElek123', 'dizelek@test.com');

INSERT INTO menetrend (allomasNev, honnan, hova, tav, erkezes, tavozas, peron) VALUES ('Szeged vasútállomás', 'Szeged', 'Szatymaz', 16, TIMESTAMP '2024-03-22 08:00:00', TIMESTAMP '2024-03-22 08:15:00', '2a');
INSERT INTO menetrend (allomasNev, honnan, hova, tav, erkezes, tavozas, peron) VALUES ('Szeged vasútállomás', 'Szeged', 'Szatymaz', 16, TIMESTAMP '2024-03-22 09:00:00', TIMESTAMP '2024-03-22 09:15:00', '3');
INSERT INTO menetrend (allomasNev, honnan, hova, tav, erkezes, tavozas, peron) VALUES ('Szeged vasútállomás', 'Szeged', 'Szatymaz', 16, TIMESTAMP '2024-03-22 10:00:00', TIMESTAMP '2024-03-22 10:15:00', '2a');
INSERT INTO menetrend (allomasNev, honnan, hova, tav, erkezes, tavozas, peron) VALUES ('Szeged vasútállomás', 'Szeged', 'Szatymaz', 16, TIMESTAMP '2024-03-22 11:00:00', TIMESTAMP '2024-03-22 11:15:00', '3');
INSERT INTO menetrend (allomasNev, honnan, hova, tav, erkezes, tavozas, peron) VALUES ('Kistelek vasútállomás', 'Kistelek', 'Kiskunfélegyháza', 29, TIMESTAMP '2024-03-22 08:00:00', TIMESTAMP '2024-03-22 08:15:00', '2');
