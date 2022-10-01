-- Creation of the table images to use the commands found in extension data.py

CREATE TABLE IF NOT EXISTS "images" (
	"image_id"	INTEGER NOT NULL UNIQUE,
	"image"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("image_id" AUTOINCREMENT)
);