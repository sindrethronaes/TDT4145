-- Sletter DB hvis den eksisterer
DROP TABLE IF EXISTS TogruterPåBanestrekning;
DROP TABLE IF EXISTS Operatør;
DROP TABLE IF EXISTS AntallVogntyper;
DROP TABLE IF EXISTS Vogn;
DROP TABLE IF EXISTS Sovevogn;
DROP TABLE IF EXISTS Sittevogn;
DROP TABLE IF EXISTS BillettISovevogn;
DROP TABLE IF EXISTS BillettISittevogn;
DROP TABLE IF EXISTS KundeOrdre;
DROP TABLE IF EXISTS Ordre;
DROP TABLE IF EXISTS Rutestopp;
DROP TABLE IF EXISTS DatoerForTogruter;
DROP TABLE IF EXISTS Kunde;
DROP TABLE IF EXISTS Delstrekning;
DROP TABLE IF EXISTS Banestrekning;
DROP TABLE IF EXISTS Dato;
DROP TABLE IF EXISTS Togrute;
DROP TABLE IF EXISTS DelstrekningIHovedretning;
DROP TABLE IF EXISTS Stasjon;

-- Lager DB
CREATE TABLE Stasjon (
	"StasjonNavn"	TEXT NOT NULL PRIMARY KEY,
	"Moh."	INT NOT NULL
);

CREATE TABLE DelstrekningIHovedretning (
	"DelstrekningID" TEXT NOT NULL PRIMARY KEY,
	"Startstasjon"	TEXT NOT NULL REFERENCES Stasjon(StasjonNavn),
	"Endestasjon" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn)
);

CREATE TABLE Togrute (
	"TogruteNavn"	TEXT PRIMARY KEY,
	"DelstrekningID"	TEXT NOT NULL REFERENCES DelstrekningIHovedretning(DelstrekningID)
);

CREATE TABLE TogruterPåBanestrekning (
	"Banestrekning"	TEXT PRIMARY KEY,
	"TogruteNavn"	TEXT NOT NULL REFERENCES Togrute(TogruteNavn)
);

CREATE TABLE Operatør (
	"OperatørNavn"	TEXT PRIMARY KEY,
	"Banestrekning"	TEXT NOT NULL REFERENCES TogruterPåBanestrekning(Banestrekning)
);

CREATE TABLE Dato (
	"Dato" DATE NOT NULL PRIMARY KEY,
	"Ukedag" TEXT NOT NULL
);

CREATE TABLE AntallVogntyper (
	"OperatørNavn" TEXT NOT NULL REFERENCES Operatør(OperatørNavn) PRIMARY KEY,
	"AntallVogntyper" INT NOT NULL
);

CREATE TABLE Banestrekning (
	"BanestrekningID" TEXT NOT NULL PRIMARY KEY,
	"BanestrekningNavn"	TEXT NOT NULL,
	"Fremdriftsenergi" TEXT NOT NULL
);

CREATE TABLE Delstrekning (
	"DelstrekningID" TEXT NOT NULL PRIMARY KEY,
	"LengdeIkm"	INT NOT NULL,
	"HarDobbbeltspor" TEXT NOT NULL
);

CREATE TABLE Vogn (
	"VognID" TEXT NOT NULL PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"TilgjengeligForBruk" TEXT NOT NULL,
	"NummerIVognsammensetning" INT NOT NULL,
	"VognType" TEXT NOT NULL,
	"OperatørNavn" TEXT NOT NULL REFERENCES Operatør(OperatørNavn)
);

CREATE TABLE Sovevogn (
	"VognID" TEXT PRIMARY KEY REFERENCES Vogn(VognID),
	"Seng"	TEXT NOT NULL
);

CREATE TABLE Sittevogn (
	"VognID" TEXT PRIMARY KEY REFERENCES Vogn(VognID),
	"Sete"	TEXT NOT NULL
);

CREATE TABLE Kunde (
	"KundeID" TEXT PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"Epost" TEXT NOT NULL,
	"Nummer" INT NOT NULL
);

CREATE TABLE KundeOrdre (
	"OrdreID" TEXT NOT NULL PRIMARY KEY,
	"Dato"	DATE NOT NULL,
	"TogruteNavn" TEXT NOT NULL REFERENCES Togrute(TogruteNavn),
	"KundeID" TEXT NOT NULL REFERENCES Kunde(KundeID)
);

CREATE TABLE BillettISittevogn (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"Sete" TEXT NOT NULL REFERENCES Sittevogn(Sete)
);

CREATE TABLE BillettISovevogn (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"Seng" TEXT NOT NULL REFERENCES Sovevogn(Seng)
);

CREATE TABLE Rutestopp (
    "TogruteNavn" TEXT NOT NULL REFERENCES Togrute(TogruteNavn),
    "StasjonNavn" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn),
    "Avgang" TIME,
    "Ankomst" TIME,
    PRIMARY KEY ("TogruteNavn", "StasjonNavn")
);

CREATE TABLE Ordre (
	"OrdreID" TEXT PRIMARY KEY,
	"BillettID" TEXT NOT NULL
);

CREATE TABLE DatoerForTogruter (
	"Togrutenavn" TEXT PRIMARY KEY REFERENCES Togrute(TogruteNavn),
	"Dato" DATE NOT NULL REFERENCES Dato(Dato)
);
