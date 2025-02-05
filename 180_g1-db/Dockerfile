FROM postgres:latest

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mylittlebank

COPY mylittlebank_db.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
