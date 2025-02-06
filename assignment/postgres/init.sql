-- Check if the user exists before creating
DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'swageruser') THEN
        CREATE ROLE swageruser WITH LOGIN ENCRYPTED PASSWORD 'Swagerdb123';
    END IF;
END
$$;

-- Check if the database exists before creating
DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'swagerdb') THEN
        CREATE DATABASE swagerdb;
    END IF;
END
$$;

