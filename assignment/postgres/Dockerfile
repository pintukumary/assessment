From postgres:14

ENV POSTGRES_USER=swagerdb
ENV POSTGRES_PASSWORD=Swagerdb123
ENV POSTGRES_DB=swagerdb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
