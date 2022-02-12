-- Database: Clinic

-- DROP DATABASE IF EXISTS "Clinic";

CREATE DATABASE "Clinic"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Canada.1252'
    LC_CTYPE = 'English_Canada.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.Branch

-- DROP TABLE IF EXISTS public."Branch";

CREATE TABLE IF NOT EXISTS public."Branch"
(
    "Phone_no" numeric NOT NULL,
    "Build_no" numeric NOT NULL,
    "Street" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Province" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Country" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Postal_code" character varying COLLATE pg_catalog."default" NOT NULL,
    "EID" BIGINT NOT NULL,
    "City" integer NOT NULL,
    CONSTRAINT "Branch_pkey" PRIMARY KEY ("City"),
    CONSTRAINT "Branch_EID_fkey" FOREIGN KEY ("EID")
        REFERENCES public."Employee" ("EID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Branch"
    OWNER to postgres;

    -- Table: public.Employee

-- DROP TABLE IF EXISTS public."Employee";

CREATE TABLE IF NOT EXISTS public."Employee"
(
    "EID" integer NOT NULL,
    "SSN" integer NOT NULL,
    "First_name" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Last_name" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Employee_type" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Salary" numeric NOT NULL,
    "Title" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Employee_pkey" PRIMARY KEY ("EID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Employee"
    OWNER to postgres;

-- Table: public.User

-- DROP TABLE IF EXISTS public."User";

CREATE TABLE IF NOT EXISTS public."User"
(
    "UserID" integer NOT NULL,
    "Email" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Username" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Password" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Last_login_time" numeric NOT NULL,
    "User_type" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "User_pkey" PRIMARY KEY ("UserID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."User"
    OWNER to postgres;