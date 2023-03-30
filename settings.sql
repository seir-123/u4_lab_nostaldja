CREATE DATABASE nostaldja;
CREATE USER nostaldjauser WITH PASSWORD 'nostaldja';
ALTER DATABASE nostaldja OWNER TO nostaldjauser;
GRANT USAGE, CREATE ON SCHEMA public TO nostaldjauser;