-- Table definitions for the catalog project.
--
-- Assumes `psql` CLI is available and connects to it.
-- Drops any previous tables/relations before creating new ones.

DROP DATABASE IF EXISTS estatecatalog;
CREATE Database estatecatalog;

\c estatecatalog;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS items CASCADE;

CREATE TABLE users(id serial primary key, name text, email text, picture text);

CREATE TABLE categories (id serial primary key, name text);

CREATE TABLE items (
  id serial primary key,
  name text,
  description text,
  value int,
  quantity int,
  disposition text,
  image text,
  categories_id int REFERENCES categories(id)
  ON DELETE CASCADE);

-- Insert statements below are run to populate the database for testing

INSERT INTO users VALUES (default,'Jason Horowitz','horowitz.jason@gmail.com', 'none');
INSERT INTO users VALUES (default,'Anouche Mardirossian','mardirossian.anouche@gmail.com', 'none');
INSERT INTO users VALUES (default,'Monica Horowitz','monicatamar93@gmail.com', 'none');
INSERT INTO users VALUES (default,'Maksim Horowitz','bklynmaks@gmail.com', 'none');


INSERT INTO categories VALUES (default,'Furniture');
INSERT INTO categories VALUES (default,'Kitchen Items');
INSERT INTO categories VALUES (default,'Bedding & Linens');
INSERT INTO categories VALUES (default,'Artwork & Decorations');
INSERT INTO categories VALUES (default,'Lighting');
INSERT INTO categories VALUES (default,'AudioVisual & Electronics');
INSERT INTO categories VALUES (default,'Other');


INSERT INTO items VALUES (default,'Queen Bed','Bed',0, 1, 'JH', 'none', 1);
INSERT INTO items VALUES (default,'Desk','Blue room',100, 1, 'MAH','none', 1);
INSERT INTO items VALUES (default,'Casserole','Copper',0, 1, 'AM','none', 2);
INSERT INTO items VALUES (default,'Painting','Squid',0, 1, 'MTH','none', 4);
INSERT INTO items VALUES (default,'Knicks Lamps','Orange, Blue', 50, 2, 'JH', 'none', 5);
INSERT INTO items VALUES (default,'Sonos','6 speakers & bridge', 400, 6, 'Sell', 'none', 6);
INSERT INTO items VALUES (default,'Russian Books','Moscow & SPB', 0, 50, 'Donate', 'none');
INSERT INTO items VALUES (default,'French Press','Moscow & SPB', 0, 1, 'AM', 'none', 2);
INSERT INTO items VALUES (default,'Queen sheets','Soft', 20, 1, 'Donate', 'none', 3);
