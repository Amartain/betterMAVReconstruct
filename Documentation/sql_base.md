
Varosok()
Allomasok()
VasutVonalak()
Megallok()
Jegyek()
Menetrendek()
Felhasznalok()


Allomasok(**id**, *varos_id* //called irsz/, nev, cim)
Varosok(**id**, nev, regio, orszag)
Megallok(**id**, *vonal_id*, nev, *elozo_id*, *kovetkezo_id*, tav_kezdotol, menetrendek_id)
VonatVonalak(**id**, nev, honnan_id, hova_id)
Jegyek(**id**, *vonal_id*, *honnan_irsz*, *hova_irsz*, *felhasznalo_id*, ar, tav, ervenyesseg_kezdete, ervenyesseg_vege, utastipus)
Menetrendek(id, megallo_id, irany, indul, erkezik_kovetkezo, peron)
Felhasznalok(**email**, nev, jelszo, utastipus)

// based on utastipus count discount on Jegy this way:
- student -50%
- senior -90%
- disability -90%
- child under 6 -100%



````sql
CREATE TABLE Varosok (
    irsz NUMBER(5) PRIMARY KEY,
    nev VARCHAR2(255),
    regio VARCHAR2(255),
    orszag VARCHAR2(255)
);

CREATE TABLE Allomasok (
    id NUMBER PRIMARY KEY,
    varos_irsz NUMBER REFERENCES Varosok(irsz),
    nev VARCHAR2(255),
    cim VARCHAR2(255)
);

CREATE TABLE VonatVonalak (
    id NUMBER PRIMARY KEY,
    nev VARCHAR2(255),
    honnan_id NUMBER REFERENCES Allomasok(id),
    hova_id NUMBER REFERENCES Allomasok(id)
);

CREATE TABLE Megallok (
    id NUMBER PRIMARY KEY,
    vonal_id NUMBER REFERENCES VonatVonalak(id),
    nev VARCHAR2(255),
    elozo_id NUMBER REFERENCES Megallok(id),
    kovetkezo_id NUMBER REFERENCES Megallok(id),
    tav_kezdotol NUMBER,
    menetrendek_id NUMBER
);

CREATE TABLE Menetrendek (
    id NUMBER PRIMARY KEY,
    megallo_id NUMBER REFERENCES Megallok(id),
    irany number(1) NOT NULL,
    indul TIMESTAMP,
    erkezik_kovetkezo TIMESTAMP,
    peron VARCHAR2(255)
);

CREATE TABLE Felhasznalok (
    email VARCHAR2(255) PRIMARY KEY,
    nev VARCHAR2(255),
    jelszo VARCHAR2(255),
    utastipus VARCHAR2(255)
);

CREATE TABLE Jegyek (
    id NUMBER PRIMARY KEY,
    vonal_id NUMBER REFERENCES VonatVonalak(id),
    honnan_irsz NUMBER REFERENCES Allomasok(varos_irsz),
    hova_irsz NUMBER REFERENCES Allomasok(varos_irsz),
    felhasznalo_id VARCHAR2(255) REFERENCES Felhasznalok(email),
    ar NUMBER,
    tav NUMBER,
    ervenyesseg_kezdete DATE,
    ervenyesseg_vege DATE,
    utastipus VARCHAR2(255)
);


SELECT j.id,
       j.vonal_id,
       j.honnan_irsz,
       j.hova_irsz,
       j.felhasznalo_id,
       CASE
           WHEN f.utastipus = 'tanulo' THEN j.ar * 0.5
           WHEN f.utastipus = 'nyugdijas' THEN j.ar * 0.1
           WHEN f.utastipus = 'kedvezmenyezett' THEN j.ar * 0.1
           WHEN f.utastipus = 'gyermek' THEN j.ar * 0.1
       END AS discounted_ar,
       j.tav,
       j.ervenyesseg_kezdete,
       j.ervenyesseg_vege,
       j.utastipus
FROM Jegyek j
JOIN Felhasznalok f ON j.felhasznalo_id = f.email;

-- Pelda adatok
-- Varosok adat
INSERT INTO Varosok (id, nev, regio, orszag) VALUES (1, 'Budapest', 'Közép-Magyarország', 'Magyarország');
INSERT INTO Varosok (id, nev, regio, orszag) VALUES (2, 'Debrecen', 'Észak-Alföld', 'Magyarország');
INSERT INTO Varosok (id, nev, regio, orszag) VALUES (3, 'Szeged', 'Dél-Alföld', 'Magyarország');

-- Allomasok
INSERT INTO Allomasok (id, varos_id, nev, cim) VALUES (1, 1, 'Keleti Pályaudvar', 'Budapest, Baross tér');
INSERT INTO Allomasok (id, varos_id, nev, cim) VALUES (2, 2, 'Nagyállomás', 'Debrecen, Petőfi tér');
INSERT INTO Allomasok (id, varos_id, nev, cim) VALUES (3, 3, 'Mars tér', 'Szeged, Mars tér 1-3');

--  VonatVonalak
INSERT INTO VonatVonalak (id, nev, honnan_id, hova_id) VALUES (1, 'InterCity', 1, 2);
INSERT INTO VonatVonalak (id, nev, honnan_id, hova_id) VALUES (2, 'Gyorsvonat', 2, 3);

-- Megallok
INSERT INTO Megallok (id, vonal_id, nev, elozo_id, kovetkezo_id, tav_kezdotol, menetrendek_id) VALUES (1, 1, 'Kőbánya-Kispest', NULL, 2, 0, NULL);
INSERT INTO Megallok (id, vonal_id, nev, elozo_id, kovetkezo_id, tav_kezdotol, menetrendek_id) VALUES (2, 1, 'Ferihegy', 1, 3, 10, NULL);

--  Menetrendek
-- 0 normal irany, 1 vissz irany
INSERT INTO Menetrendek (id, megallo_id, irany, indul, erkezik_kovetkezo, peron) VALUES (1, 1, 0, TO_TIMESTAMP('08:00:00', 'HH24:MI:SS'), TO_TIMESTAMP('08:15:00', 'HH24:MI:SS'), '5a');
INSERT INTO Menetrendek (id, megallo_id, irany, indul, erkezik_kovetkezo, peron) VALUES (2, 2, 1, TO_TIMESTAMP('09:00:00', 'HH24:MI:SS'), TO_TIMESTAMP('09:20:00', 'HH24:MI:SS'), '2b');


-- Felhasznalok
INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES ('janos@example.com', 'Kovács János', 'titkos123', 'student');
INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES ('erika@example.com', 'Nagy Erika', 'jelszo456', 'senior');

-- Jegyek
INSERT INTO Jegyek (id, vonal_id, honnan_irsz, hova_irsz, felhasznalo_id, ar, tav, ervenyesseg_kezdete, ervenyesseg_vege, utastipus) VALUES (1, 1, 1, 2, 'janos@example.com', 3000, 195, TO_DATE('2024-04-01', 'YYYY-MM-DD'), TO_DATE('2024-04-30', 'YYYY-MM-DD'), 'student');
INSERT INTO Jegyek (id, vonal_id, honnan_irsz, hova_irsz, felhasznalo_id, ar, tav, ervenyesseg_kezdete, ervenyesseg_vege, utastipus) VALUES (2, 2, 2, 3, 'erika@example.com', 2500, 150, TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-05-31', 'YYYY-MM-DD'), 'senior');


```