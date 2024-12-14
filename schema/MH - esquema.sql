--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

-- Started on 2022-07-11 00:18:35

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
-- TOC entry 209 (class 1259 OID 24674)
-- Name: amigato; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.amigato (
    id integer NOT NULL,
    nome character varying NOT NULL,
    nivel integer NOT NULL,
    cor_pelo character varying NOT NULL,
    cor_olho character varying NOT NULL,
    cacador_id integer NOT NULL
);


ALTER TABLE public.amigato OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 24679)
-- Name: arma; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.arma (
    id integer NOT NULL,
    tipo character varying NOT NULL,
    elemento character varying NOT NULL,
    forca integer NOT NULL,
    nome character varying NOT NULL,
    monstro_id integer NOT NULL
);


ALTER TABLE public.arma OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 24684)
-- Name: cacador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cacador (
    id integer NOT NULL,
    rank integer NOT NULL,
    nome character varying NOT NULL
);


ALTER TABLE public.cacador OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 24689)
-- Name: cacador_arma; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cacador_arma (
    cacador_id integer NOT NULL,
    arma_id integer NOT NULL
);


ALTER TABLE public.cacador_arma OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 24692)
-- Name: cacador_missao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cacador_missao (
    cacador_id integer NOT NULL,
    missao_id integer NOT NULL
);


ALTER TABLE public.cacador_missao OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 24695)
-- Name: missao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao (
    id integer NOT NULL,
    nome character varying NOT NULL,
    dificuldade integer NOT NULL,
    tempo time without time zone NOT NULL
);


ALTER TABLE public.missao OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 24700)
-- Name: missao_monstro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_monstro (
    missao_id integer NOT NULL,
    monstro_id integer NOT NULL,
    quantidade_monstro integer NOT NULL
);


ALTER TABLE public.missao_monstro OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 24703)
-- Name: monstro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monstro (
    id integer NOT NULL,
    tipo character varying NOT NULL,
    elemento character varying NOT NULL,
    tamanho numeric NOT NULL,
    nome character varying NOT NULL,
    imagem character varying
);


ALTER TABLE public.monstro OWNER TO postgres;

--
-- TOC entry 3192 (class 2606 OID 24709)
-- Name: amigato amigato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.amigato
    ADD CONSTRAINT amigato_pkey PRIMARY KEY (id);


--
-- TOC entry 3194 (class 2606 OID 24711)
-- Name: arma arma_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arma
    ADD CONSTRAINT arma_pkey PRIMARY KEY (id);


--
-- TOC entry 3198 (class 2606 OID 24713)
-- Name: cacador_arma cacador_arma_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_arma
    ADD CONSTRAINT cacador_arma_pkey PRIMARY KEY (cacador_id, arma_id);


--
-- TOC entry 3202 (class 2606 OID 24715)
-- Name: cacador_missao cacador_missao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_missao
    ADD CONSTRAINT cacador_missao_pkey PRIMARY KEY (cacador_id, missao_id);


--
-- TOC entry 3196 (class 2606 OID 24717)
-- Name: cacador cacador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador
    ADD CONSTRAINT cacador_pkey PRIMARY KEY (id);


--
-- TOC entry 3210 (class 2606 OID 24719)
-- Name: missao_monstro missao_monstro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_monstro
    ADD CONSTRAINT missao_monstro_pkey PRIMARY KEY (missao_id, monstro_id);


--
-- TOC entry 3206 (class 2606 OID 24721)
-- Name: missao missao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao
    ADD CONSTRAINT missao_pkey PRIMARY KEY (id);


--
-- TOC entry 3212 (class 2606 OID 24723)
-- Name: monstro monstro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monstro
    ADD CONSTRAINT monstro_pkey PRIMARY KEY (id);


--
-- TOC entry 3199 (class 1259 OID 24724)
-- Name: fki_cacador_arma_arma_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_cacador_arma_arma_id_fkey ON public.cacador_arma USING btree (arma_id);


--
-- TOC entry 3200 (class 1259 OID 24725)
-- Name: fki_cacador_arma_cacador_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_cacador_arma_cacador_id_fkey ON public.cacador_arma USING btree (cacador_id);


--
-- TOC entry 3203 (class 1259 OID 24726)
-- Name: fki_cacador_missao_cacador_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_cacador_missao_cacador_id_fkey ON public.cacador_missao USING btree (cacador_id);


--
-- TOC entry 3204 (class 1259 OID 24727)
-- Name: fki_cacador_missao_missao_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_cacador_missao_missao_id_fkey ON public.cacador_missao USING btree (missao_id);


--
-- TOC entry 3207 (class 1259 OID 24728)
-- Name: fki_missao_monstro_missao_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_missao_monstro_missao_id_fkey ON public.missao_monstro USING btree (missao_id);


--
-- TOC entry 3208 (class 1259 OID 24729)
-- Name: fki_missao_monstro_monstro_id_fkey; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_missao_monstro_monstro_id_fkey ON public.missao_monstro USING btree (monstro_id);


--
-- TOC entry 3213 (class 2606 OID 24730)
-- Name: amigato amigato_cacador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.amigato
    ADD CONSTRAINT amigato_cacador_id_fkey FOREIGN KEY (cacador_id) REFERENCES public.cacador(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3214 (class 2606 OID 24735)
-- Name: arma arma_monstro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arma
    ADD CONSTRAINT arma_monstro_id_fkey FOREIGN KEY (monstro_id) REFERENCES public.monstro(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3215 (class 2606 OID 24740)
-- Name: cacador_arma cacador_arma_arma_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_arma
    ADD CONSTRAINT cacador_arma_arma_id_fkey FOREIGN KEY (arma_id) REFERENCES public.arma(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3216 (class 2606 OID 24745)
-- Name: cacador_arma cacador_arma_cacador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_arma
    ADD CONSTRAINT cacador_arma_cacador_id_fkey FOREIGN KEY (cacador_id) REFERENCES public.cacador(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3217 (class 2606 OID 24750)
-- Name: cacador_missao cacador_missao_cacador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_missao
    ADD CONSTRAINT cacador_missao_cacador_id_fkey FOREIGN KEY (cacador_id) REFERENCES public.cacador(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3218 (class 2606 OID 24755)
-- Name: cacador_missao cacador_missao_missao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cacador_missao
    ADD CONSTRAINT cacador_missao_missao_id_fkey FOREIGN KEY (missao_id) REFERENCES public.missao(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3219 (class 2606 OID 24760)
-- Name: missao_monstro missao_monstro_missao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_monstro
    ADD CONSTRAINT missao_monstro_missao_id_fkey FOREIGN KEY (missao_id) REFERENCES public.missao(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3220 (class 2606 OID 24765)
-- Name: missao_monstro missao_monstro_monstro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_monstro
    ADD CONSTRAINT missao_monstro_monstro_id_fkey FOREIGN KEY (monstro_id) REFERENCES public.monstro(id) ON UPDATE CASCADE ON DELETE RESTRICT;


-- Completed on 2022-07-11 00:18:35

--
-- PostgreSQL database dump complete
--

