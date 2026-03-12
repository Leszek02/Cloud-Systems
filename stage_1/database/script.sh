
docker cp ./database.sql cloud-db:/
docker cp ./TSLA.csv cloud-db:/

MSYS_NO_PATHCONV=1 docker exec cloud-db chmod 744 /TSLA.csv
MSYS_NO_PATHCONV=1 docker exec -i cloud-db psql -U postgres -f /database.sql