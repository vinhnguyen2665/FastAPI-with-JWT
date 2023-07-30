-- Table: public.tbl_users

-- DROP TABLE IF EXISTS public.tbl_users;

CREATE TABLE IF NOT EXISTS public.tbl_users
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    full_name character(40) COLLATE pg_catalog."default",
    email character(40) COLLATE pg_catalog."default" NOT NULL,
    delete_flg character(1) COLLATE pg_catalog."default" NOT NULL DEFAULT false,
    password character(300) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tbl_users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_users
    OWNER to postgres;