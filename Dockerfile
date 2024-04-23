FROM postgres:16.2

COPY databases/postgre/init.sql /docker-entrypoint-initdb.d/
