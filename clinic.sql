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