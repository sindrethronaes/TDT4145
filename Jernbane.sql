-- Deletes DB if it alreadt exists
DROP TABLE IF EXISTS TogruterPaaBanestrekning;
DROP TABLE IF EXISTS Operatoer;
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
DROP TABLE IF EXISTS Kupe;
DROP TABLE IF EXISTS Sete;
DROP TABLE IF EXISTS Seng;
DROP TABLE IF EXISTS SeteIVogn;
DROP TABLE IF EXISTS SengIKupe;

-- Creates DB
CREATE TABLE Stasjon (
	"StasjonNavn"	TEXT NOT NULL PRIMARY KEY,
	"Moh."	INT NOT NULL
);

CREATE TABLE DelstrekningIHovedretning (
	"DelstrekningID" TEXT PRIMARY KEY REFERENCES Delstrekning(DelstrekningID),
	"Startstasjon"	TEXT NOT NULL REFERENCES Stasjon(StasjonNavn),
	"Endestasjon" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn)
);

CREATE TABLE Togrute (
	"TogruteNavn"	TEXT PRIMARY KEY,
	"DelstrekningID"	TEXT NOT NULL REFERENCES DelstrekningIHovedretning(DelstrekningID)
);

CREATE TABLE TogruterPaaBanestrekning (
	"Banestrekning"	TEXT REFERENCES Banestrekning(BanestrekningID),
	"TogruteNavn"	TEXT REFERENCES Togrute(TogruteNavn),
	PRIMARY KEY ("Banestrekning", "TogruteNavn")
);


CREATE TABLE Operatoer (
	"OperatoerNavn"	TEXT PRIMARY KEY,
	"Banestrekning"	TEXT NOT NULL REFERENCES TogruterPaaBanestrekning(Banestrekning)
);

CREATE TABLE Dato (
	"Dato" DATE NOT NULL PRIMARY KEY,
	"Ukedag" TEXT NOT NULL
);

CREATE TABLE AntallVogntyper (
	"OperatoerNavn" TEXT REFERENCES Operatoer(OperatoerNavn) PRIMARY KEY,
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
	"HarDobbbeltspor" BOOLEAN NOT NULL
);

CREATE TABLE Vogn (
	"VognID" INT PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"TilgjengeligForBruk" BOOLEAN NOT NULL,
	"NummerIVognsammensetning" INT,
	"VognType" TEXT NOT NULL,
	"OperatoerNavn" TEXT NOT NULL REFERENCES Operatoer(OperatoerNavn)
);

CREATE TABLE Sovevogn (
	"VognID" INT PRIMARY KEY REFERENCES Vogn(VognID),
	"AntallSenger" INT NOT NULL,
	"SengerPerKupe" INT NOT NULL
);

CREATE TABLE Sittevogn (
	"VognID" INT PRIMARY KEY REFERENCES Vogn(VognID),
	"AntallSeter" INT NOT NULL,
	"SeterPerVogn" INT NOT NULL
);

--SUGGESTION OF NEW TABLE
CREATE TABLE Kupe  (
	"KupeID" INT,
	"VognID" INT REFERENCES Vogn(VognID),
	"AntallSenger" INT NOT NULL,
	"Tilgjengelig" BOOLEAN,
	PRIMARY KEY ("KupeID", "VognID")
);

-- SUGGESTION OF NEW TABLE
CREATE TABLE Seng (
	"SengID" INT NOT NULL,
	"KupeID" INT NOT NULL REFERENCES Kupe(KupeID),
	"VognID" INT REFERENCES Vogn(VognID),
	"Tilgjengelig" BOOLEAN,
	FOREIGN KEY ("KupeID", "VognID") REFERENCES Kupe(KupeID, VognID),
	PRIMARY KEY ("SengID", "KupeID", "VognID")
);

-- SUGGESTION OF NEW TABLE
CREATE TABLE Sete (
	"SeteID" INT,
	"VognID" INT REFERENCES Vogn(VognID),
	"Tilgjengelig" TEXT NOT NULL,
	PRIMARY KEY ("SeteID", "VognID")
);

CREATE TABLE Kunde (
	"KundeID" TEXT PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"Epost" TEXT NOT NULL,
	"Nummer" INT NOT NULL
);

CREATE TABLE KundeOrdre (
	"OrdreID" TEXT NOT NULL PRIMARY KEY,
	"Dato"	DATE NOT NULL REFERENCES Dato(Dato),
	"TogruteNavn" TEXT NOT NULL REFERENCES Togrute(TogruteNavn),
	"KundeID" TEXT NOT NULL REFERENCES Kunde(KundeID)
);

CREATE TABLE BillettISittevogn (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"SeteID" TEXT NOT NULL REFERENCES Sete(SeteID)
);

CREATE TABLE BillettISovevogn (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"SengID" TEXT NOT NULL REFERENCES Seng(SengID)
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