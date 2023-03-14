CREATE TABLE "Stasjon" (
	"StasjonNavn"	TEXT NOT NULL PRIMARY KEY,
	"Moh."	INT NOT NULL

);

CREATE TABLE "DelstrekningIHovedretning" (
	"DelstrekningID" TEXT NOT NULL PRIMARY KEY,
	"Startstasjon"	TEXT NOT NULL ,
	"Endestasjon" TEXT NOT NULL ,
	FOREIGN KEY(Endestasjon)REFERENCES stasjon(StasjonNavn),
	FOREIGN KEY(Startstasjon)REFERENCES stasjon(StasjonNavn)
);

CREATE TABLE "Togrute" (
	"TogruteNavn"	TEXT NOT NULL PRIMARY KEY,
	"DelstrekningID"	TEXT NOT NULL,
	FOREIGN KEY(DelstrekningID)REFERENCES DelstrekningIHovedretning(DelstrekningID)
);


CREATE TABLE "TogruterPåBanestrekning" (
	"Banestrekning"	TEXT NOT NULL PRIMARY KEY,
	"TogruteNavn"	TEXT NOT NULL,
	FOREIGN KEY(TogruteNavn)REFERENCES Togrute(TogruteNavn)
	);

CREATE TABLE "Operatører" (
	"OperatørerNavn"	TEXT NOT NULL PRIMARY KEY,
	"Banestrekning"	TEXT NOT NULL REFERENCES TogruterPåBanestrekning(Banestrekning),
	);

CREATE TABLE "Datoer" (
	"Dato" date NOT NULL PRIMARY KEY,
	"Ukedag"	TEXT NOT NULL
	);

CREATE TABLE "AntallVogntyper" (
	"OperatørerNavn" PRIMARY KEY,
	AntallVogntyper INT NOT NULL
	);

CREATE TABLE "Banestrekning" (
	"BanestrekningID" TEXT NOT NULL PRIMARY KEY,
	"BanestrekningNavn"	TEXT NOT NULL,
	"Fremdriftsenergi" TEXT NOT NULL
	);

CREATE TABLE "DeltrekningInfo" (
	"DelstrekningID" TEXT NOT NULL PRIMARY KEY,
	"LengdeIkm"	INT NOT NULL,
	"HarDobbbeltspor" TEXT NOT NULL
	);

CREATE TABLE "Vogn" (
	"VognID" TEXT NOT NULL PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"OperatørerNavn" TEXT NOT NULL,
	"TilgjengeligForBruk" TEXT NOT NULL,
	"NummerIVognsammensetning" INT NOT NULL,
	"VognType" TEXT NOT NULL,
	FOREIGN KEY (OperatørerNavn) REFERENCES Operatører(OperatørerNavn)
	);

CREATE TABLE "Sovevogn" (
	"VognID" TEXT NOT NULL PRIMARY KEY,
	"Seng"	TEXT NOT NULL
	);

CREATE TABLE "Sittevogn" (
	"VognID" TEXT NOT NULL PRIMARY KEY,
	"Sete"	TEXT NOT NULL
	);


CREATE TABLE "Kunde" (
	"KundeID" TEXT NOT NULL PRIMARY KEY,
	"Navn"	TEXT NOT NULL,
	"E-post" TEXT NOT NULL,
	"Number" INT NOT NULL
	);

CREATE TABLE "KundeOrdre" (
	"OrdreID" TEXT NOT NULL PRIMARY KEY,
	"Dato"	date NOT NULL,
	"TogruteNavn" TEXT NOT NULL,
	"KundeID" TEXT NOT NULL,
	FOREIGN KEY (TogruteNavn) REFERENCES Togrute(TogruteNavn),
	FOREIGN KEY (KundeID) REFERENCES Kunde(KundeID)
	);

CREATE TABLE "BillettISittevogn" (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"Sete" TEXT NOT NULL,
	FOREIGN KEY (Sete) REFERENCES Sittevogn(Sete)
	);

CREATE TABLE "BillettISovevogn" (
	"BillettID" TEXT NOT NULL PRIMARY KEY,
	"Seng" TEXT NOT NULL,
	FOREIGN KEY (Seng) REFERENCES Sovevogn(Seng)
	);



CREATE TABLE "Rutestopp" (
	"TogruteNavn" TEXT NOT NULL,
	"StasjonNavn" TEXT NOT NULL,
	"Avgang" time NOT NULL,
	"Ankomst" time NOT NULL,
	PRIMARY KEY(TogruteNavn, StasjonNavn)
	);


CREATE TABLE "Ordre" (
	"OrdreID" TEXT NOT NULL PRIMARY KEY,
	"BillettID" TEXT NOT NULL
	);


CREATE TABLE "DatoerForTogruter" (
	"Togrutenavn" TEXT NOT NULL PRIMARY KEY,
	"Dato" date NOT NULL,
	FOREIGN KEY (Dato) REFERENCES Datoer(Dato)
	);

