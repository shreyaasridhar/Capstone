--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dishes; Type: TABLE; Schema: public; Owner: shreyaasridhar
--

CREATE TABLE public.dishes (
    id integer NOT NULL,
    name character varying NOT NULL,
    image_link character varying,
    ingredients character varying NOT NULL
);


ALTER TABLE public.dishes OWNER TO shreyaasridhar;

--
-- Name: dishes_id_seq; Type: SEQUENCE; Schema: public; Owner: shreyaasridhar
--

CREATE SEQUENCE public.dishes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dishes_id_seq OWNER TO shreyaasridhar;

--
-- Name: dishes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shreyaasridhar
--

ALTER SEQUENCE public.dishes_id_seq OWNED BY public.dishes.id;


--
-- Name: ingredients; Type: TABLE; Schema: public; Owner: shreyaasridhar
--

CREATE TABLE public.ingredients (
    id integer NOT NULL,
    name character varying NOT NULL,
    image_link character varying,
    color character varying
);


ALTER TABLE public.ingredients OWNER TO shreyaasridhar;

--
-- Name: ingredients_id_seq; Type: SEQUENCE; Schema: public; Owner: shreyaasridhar
--

CREATE SEQUENCE public.ingredients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingredients_id_seq OWNER TO shreyaasridhar;

--
-- Name: ingredients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shreyaasridhar
--

ALTER SEQUENCE public.ingredients_id_seq OWNED BY public.ingredients.id;


--
-- Name: dishes id; Type: DEFAULT; Schema: public; Owner: shreyaasridhar
--

ALTER TABLE ONLY public.dishes ALTER COLUMN id SET DEFAULT nextval('public.dishes_id_seq'::regclass);


--
-- Name: ingredients id; Type: DEFAULT; Schema: public; Owner: shreyaasridhar
--

ALTER TABLE ONLY public.ingredients ALTER COLUMN id SET DEFAULT nextval('public.ingredients_id_seq'::regclass);


--
-- Data for Name: dishes; Type: TABLE DATA; Schema: public; Owner: shreyaasridhar
--

COPY public.dishes (id, name, image_link, ingredients) FROM stdin;
1	penne pasta		["pasta", "tomato", "onion"]
\.


--
-- Data for Name: ingredients; Type: TABLE DATA; Schema: public; Owner: shreyaasridhar
--

COPY public.ingredients (id, name, image_link, color) FROM stdin;
1	tomato	https://images.unsplash.com/photo-1518977822534-7049a61ee0c2	red
\.


--
-- Name: dishes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shreyaasridhar
--

SELECT pg_catalog.setval('public.dishes_id_seq', 1, true);


--
-- Name: ingredients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shreyaasridhar
--

SELECT pg_catalog.setval('public.ingredients_id_seq', 1, true);


--
-- Name: dishes dishes_pkey; Type: CONSTRAINT; Schema: public; Owner: shreyaasridhar
--

ALTER TABLE ONLY public.dishes
    ADD CONSTRAINT dishes_pkey PRIMARY KEY (id);


--
-- Name: ingredients ingredients_pkey; Type: CONSTRAINT; Schema: public; Owner: shreyaasridhar
--

ALTER TABLE ONLY public.ingredients
    ADD CONSTRAINT ingredients_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

