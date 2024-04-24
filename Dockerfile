FROM postgres:16.2

COPY app/databases/postgresql/scripts/init.sql /docker-entrypoint-initdb.d/
