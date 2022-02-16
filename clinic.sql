-- Table: public.Users

-- DROP TABLE IF EXISTS public."Users";

CREATE TABLE IF NOT EXISTS public."Users"
(
    "UserID" integer NOT NULL,
    "Email" character varying(40) COLLATE pg_catalog."default" NOT NULL,
    "Username" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Password" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    "Last_login_time" numeric NOT NULL,
    "User_type" character varying(25) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "User_pkey" PRIMARY KEY ("UserID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Users"
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
)INHERITS ("Users")

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Employee"
    OWNER to postgres;
	
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
    "EID" integer NOT NULL,
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
	
CREATE TABLE IF NOT EXISTS public."Patient"
(
	"PatientID" integer NOT NULL,
	"SSN_patient" integer NOT NULL,
	"House_no" integer NOT NULL,
	"Street" character varying(40) COLLATE pg_catalog."default" NOT NULL,
	"City_name" character varying(25) COLLATE pg_catalog."default" NOT NULL,
	"Province" character varying(25) COLLATE pg_catalog."default" NOT NULL,
	"First_name" character varying(25) COLLATE pg_catalog."default" NOT NULL,
	"Last_name" character varying(25) COLLATE pg_catalog."default" NOT NULL,
	"Gender" character varying(25) COLLATE pg_catalog."default" NOT NULL,
	"Email_patient" character varying(40) COLLATE pg_catalog."default" NOT NULL,
	"Dob" date NOT NULL,
	"Phone_no_patient" numeric NOT NULL,
	CONSTRAINT "Patient_pkey" PRIMARY KEY ("PatientID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Patient"
	OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public."Insurance_claim"
(
	"ClaimID" integer NOT NULL,
	"PatientID" integer NOT NULL,
	"Claim_amount" numeric NOT NULL,
	CONSTRAINT "Insurance_claim_pkey" PRIMARY KEY ("ClaimID"),
	CONSTRAINT "Insurance_Claim_PatientID_fkey" FOREIGN KEY ("PatientID")
        REFERENCES public."Patient" ("PatientID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Insurance_Claim"
	OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public."Review"
(
	"ReviewID" integer NOT NULL,
	"PatientID" integer NOT NULL,
	"Professionalism" character varying(200) COLLATE pg_catalog."default" NOT NULL,
	"Communication" character varying(200) COLLATE pg_catalog."default" NOT NULL,
	"Cleanliness" character varying(200) COLLATE pg_catalog."default" NOT NULL,
	"Value" character varying(200) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT "Review_pkey" PRIMARY KEY ("ReviewID"),
	CONSTRAINT "Review_PatientID_fkey" FOREIGN KEY ("PatientID")
		REFERENCES public."Patient" ("PatientID") MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Review"
	OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Treatment"
(
	"TreatmentID" integer NOT NULL,
	"Treatment_type" character varying(100) COLLATE pg_catalog."default" NOT NULL,
	"Appointment_type" character varying(100) COLLATE pg_catalog."default" NOT NULL,
	"Medication" character varying(100) COLLATE pg_catalog."default" NOT NULL,
	"Symptoms" character varying(100) COLLATE pg_catalog."default" NOT NULL,
	"Tooth" character varying(100) COLLATE pg_catalog."default" NOT NULL,
	"Description" character varying(200) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT "TreatmentID_pkey" PRIMARY KEY ("TreatmentID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Treatment"
	OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Appointment"
(
	"AppointmentID" integer NOT NULL,
	"EID" integer NOT NULL,
	"PatientID" integer NOT NULL,
	"TreatmentID" integer NOT NULL,
	"Date" date NOT NULL,
	"Room" integer NOT NULL,
	"Start_time" time NOT NULL,
	"End_time" time NOT NULL,
	"Appointment_type" character varying (100) COLLATE pg_catalog."default" NOT NULL,
	"Status" character varying (100) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT "AppointmentID_pkey" PRIMARY KEY ("AppointmentID"),
	CONSTRAINT "EID_fkey" FOREIGN KEY ("EID")
		REFERENCES public."Employee" ("EID") MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT "PatientID_fkey" FOREIGN KEY ("PatientID")
		REFERENCES public."Patient" ("PatientID") MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT "TreatmentID_fkey" FOREIGN KEY ("TreatmentID")
		REFERENCES public."Treatment" ("TreatmentID") MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Appointment"
	OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Record"
(
	"RecordID" integer NOT NULL,
	"AppointmentID" integer NOT NULL,
	"Treatment_length" time NOT NULL,
	"Treatment_type" character varying (100) COLLATE pg_catalog."default" NOT NULL,
	"Patient_status" character varying (100) COLLATE pg_catalog."default"  NOT NULL,
	"Date" date NOT NULL,
	CONSTRAINT "RecordID_pkey" PRIMARY KEY ("RecordID"),
	CONSTRAINT "Record_AppointmentID_fkey" FOREIGN KEY ("AppointmentID")
		REFERENCES public."Appointment" ("AppointmentID") MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Record"
	OWNER to postgres;