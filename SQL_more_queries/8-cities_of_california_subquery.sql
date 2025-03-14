-- lists all the cities of Callifornia
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
