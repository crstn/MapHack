SELECT *
FROM parkomat
WHERE ST_DWITHIN(
	ST_SetSRID(ST_MakePoint(12.555122317280622, 55.67211257752474), 4326)::geography, geom::geography, 1000)
ORDER BY ST_DISTANCE(ST_SetSRID(
	ST_MakePoint(12.555122317280622, 55.67211257752474), 4326)::geography, geom::geography)
LIMIT 1;
