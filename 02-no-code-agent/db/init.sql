-- Databáze vozového parku (PostgreSQL i SQLite)
CREATE TABLE lokality (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    mesto TEXT NOT NULL
);

CREATE TABLE vozidla (
    id INTEGER PRIMARY KEY,
    spz TEXT NOT NULL UNIQUE,
    znacka TEXT NOT NULL,
    model TEXT NOT NULL,
    typ_pohonu TEXT NOT NULL,
    kapacita_osob INTEGER NOT NULL,
    stav_km INTEGER NOT NULL,
    km_posledni_servis INTEGER NOT NULL,
    servis_interval INTEGER NOT NULL DEFAULT 15000,
    lokalita_id INTEGER NOT NULL REFERENCES lokality(id),
    stav TEXT NOT NULL            -- Dostupné, V servisu, Vyřazeno
);

CREATE TABLE rezervace (
    id INTEGER PRIMARY KEY,
    vozidlo_id INTEGER NOT NULL REFERENCES vozidla(id),
    ridic TEXT NOT NULL,
    datum_od DATE NOT NULL,
    datum_do DATE NOT NULL,
    ucel TEXT NOT NULL,
    stav TEXT NOT NULL,           -- Čeká na schválení, Schváleno, Zamítnuto, Vráceno
    najeto_km INTEGER
);

INSERT INTO lokality VALUES (1,'Sídlo Brno','Brno'), (2,'Pracoviště Praha','Praha');

INSERT INTO vozidla VALUES
 (1,'7B1 2345','Škoda','Octavia Combi','Nafta',5,84210,75000,15000,1,'Dostupné'),
 (2,'7B2 6789','Škoda','Enyaq iV 80','Elektromobil',5,31950,30000,30000,1,'Dostupné'),
 (3,'8B3 1122','Toyota','Corolla TS','Hybrid',5,58400,45000,15000,1,'V servisu'),
 (4,'9A4 3344','Škoda','Superb','Benzín',5,122300,120000,15000,2,'Dostupné'),
 (5,'9A5 5566','Volkswagen','Transporter','Nafta',9,143800,129500,15000,2,'Dostupné');

INSERT INTO rezervace VALUES
 (1,1,'Jan Novák','2026-07-14','2026-07-15','Školení Praha','Vráceno',412),
 (2,4,'Tomáš Dvořák','2026-08-20','2026-08-22','Audit Ostrava','Vráceno',790),
 (3,1,'Jan Novák','2026-09-09','2026-09-09','Konference Zlín','Vráceno',205),
 (4,2,'Lucie Černá','2026-12-01','2026-12-02','Jednání Praha','Schváleno',NULL),
 (5,5,'Petra Svobodová','2026-12-08','2026-12-10','Stěhování','Čeká na schválení',NULL);