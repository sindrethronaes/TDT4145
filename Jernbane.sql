-- Sletter DB

DROP TABLE {Stasjon, DelstrekningIHovedretning, Togrute, TogruterPåBanestrekning, Operatører, Datoer, AntallVogntyper, Banestrekning, DelstrekningID, Vogn, Sovevogn, Sittevogn, Kunde, KundeOrdre, BillettISittevogn, BillettISovevogn, Rutestopp, Ordre, DatoerForTogruter}

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
	"Banestrekning"	TEXT NOT NULL REFERENCES TogruterPåBanestrekning(Banestrekning),
	);

CREATE TABLE Dato (
	"Dato" DATE NOT NULL PRIMARY KEY,
	"Ukedag" TEXT NOT NULL
	);

CREATE TABLE AntallVogntyper (
	"OperatørNavn" PRIMARY KEY REFERENCES Operatør(OperatørNavn),
	"AntallVogntyper" INT NOT NULL
	);

CREATE TABLE Banestrekning (
	"BanestrekningID" TEXT NOT NULL PRIMARY KEY,
	"BanestrekningNavn"	TEXT NOT NULL,
	"Fremdriftsenergi" TEXT NOT NULL
	);

CREATE TABLE Deltrekning (
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
	"OperatørerNavn" TEXT NOT NULL REFERENCES Operatør(OperatørerNavn)
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
	"TogruteNavn" TEXT PRIMARY KEY REFERENCES Togrute(TogruteNavn),
	"StasjonNavn" TEXT PRIMARY KEY REFERENCES Stasjon(StasjonNavn),
	"Avgang" time NOT NULL,
	"Ankomst" time NOT NULL,
	);


CREATE TABLE Ordre (
	"OrdreID" TEXT PRIMARY KEY,
	"BillettID" TEXT NOT NULL
	);


CREATE TABLE DatoerForTogruter (
	"Togrutenavn" TEXT PRIMARY KEY REFERENCES Togrute(TogruteNavn),
	"Dato" DATE NOT NULL REFERENCES Dato(Dato)
	);

