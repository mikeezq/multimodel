docker build -t local-postgres .
docker run --name local-db -p 5432:5432 -e POSTGRES_USER=local-db -e POSTGRES_PASSWORD=local-db -e POSTGRES_DB=local-db -d local-postgres