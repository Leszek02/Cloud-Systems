
docker cp ./database.sql postgres-db:/
docker cp ./TSLA.csv postgres-db:/

MSYS_NO_PATHCONV=1 docker exec postgres-db chmod 744 /TSLA.csv
MSYS_NO_PATHCONV=1 docker exec -i postgres-db psql -U postgres -f /database.sql