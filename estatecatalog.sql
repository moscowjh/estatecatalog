-- Table definitions for the catalog project.
--
-- Assumes `psql` CLI is available and connects to it.
-- Drops any previous tables/relations before creating new ones.

/*
\c estatecatalog;
DROP TABLE IF EXISTS user CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS items CASCADE;

/
-- create tables `categories` and `items`

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
  ON DELETE CASCADE
);
*/
/*
-- `standings` is the view called by 'playerStandings()' in `tournament.py`

CREATE VIEW standings AS
    SELECT id,
           name,
           (SELECT count(*) FROM matches WHERE players.id = matches.winner) AS wins,
           (SELECT count(*) FROM matches WHERE players.id = matches.winner OR
           players.id = matches.loser) AS matches
    FROM players
    ORDER BY wins DESC;

-- `rank` view is used to create 'pairings' for the swissPairings function in
-- `tournament.py`

CREATE VIEW rank AS
    SELECT row_number() OVER (ORDER BY wins DESC), id, name, wins FROM standings;

CREATE VIEW pairings AS
    SELECT a.id AS aid, a.name AS aname, b.id AS bid, b.name AS bname
    FROM rank as a, rank as b WHERE a.row_number % 2 = 0
    AND a.row_number-1 = b.row_number;
*/
-- Insert statements below are run to populate the database for testing

INSERT INTO users VALUES (default,'Jason Horowitz','horowitz.jason@gmail.com', 'none');
INSERT INTO users VALUES (default,'Anouche Mardirossian','mardir0ssian.anouche@gmail.com', 'none');
INSERT INTO users VALUES (default,'Monica Horowitz','monicatamar93@gmail.com', 'none');
INSERT INTO users VALUES (default,'Maksim Horowitz','bklynmaks@gmail.com', 'none');


INSERT INTO categories VALUES (default,'Furniture');
INSERT INTO categories VALUES (default,'Kitchen Items');
INSERT INTO categories VALUES (default,'Bedding & Linens');
INSERT INTO categories VALUES (default,'Artwork & Decorations');
INSERT INTO categories VALUES (default,'Lighting');
INSERT INTO categories VALUES (default,'AudioVisual & Electronics');
INSERT INTO categories VALUES (default,'Other');


INSERT INTO items VALUES (default,'Queen Bed','Bed',0, 1, 'JH', 'none', 1, 1);
INSERT INTO items VALUES (default,'Desk','Blue room',100, 1, 'MAH','none', 1, 2);
INSERT INTO items VALUES (default,'Casserole','Copper',0, 1, 'AM','none', 2, 3);
INSERT INTO items VALUES (default,'Painting','Squid',0, 1, 'MTH','none', 4, 2);
INSERT INTO items VALUES (default,'Knicks Lamps','Orange, Blue', 50, 2, 'JH', 'none', 5, 4);
INSERT INTO items VALUES (default,'Sonos','6 speakers & bridge', 400, 6, 'Sell', 'none', 6, 4);
INSERT INTO items VALUES (default,'Russian Books','Moscow & SPB', 0, 50, 'Donate', 'none', 7);
INSERT INTO items VALUES (default,'French Press','Moscow & SPB', 0, 1, 'AM', 'none', 2, 3);
INSERT INTO items VALUES (default,'Queen sheets','Soft', 20, 1, 'Donate', 'none', 3, 2);


/* following views  - `win_count`, `matches_played`, and 'standings' are an
alternate implementation of the playerStandings functionaliy but failed unit
test because players were not appearing in standings before any matches played.
Leaving this in the file in case someone wants to work on it further.

CREATE VIEW win_count AS
    SELECT winner, COALESCE(count(*),0) as wins
    FROM matches, players WHERE players.id = matches.winner
    GROUP BY winner
    ORDER BY wins DESC;

CREATE VIEW matches_played AS
    SELECT players.id, name, COALESCE(count(*),0) AS matches
    FROM matches, players
    WHERE players.id = matches.winner OR players.id = matches.loser
    GROUP BY players.id
    ORDER BY matches DESC;

-- create view 'standings' which is called by `playerStandings()` in tournament.py

CREATE VIEW standings AS
    SELECT matches_played.id, matches_played.name, COALESCE (win_count.wins,0)
    AS wins, COALESCE (matches_played.matches,0) AS matches
    FROM matches_played LEFT JOIN win_count
    ON matches_played.id = win_count.winner OR wins=0
    ORDER BY wins DESC; */
