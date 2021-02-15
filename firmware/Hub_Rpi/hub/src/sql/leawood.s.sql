--------------------------------------------------------
--  File created - Sunday-February-14-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Package LEAWOOD
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE PACKAGE "LEAWOOD_DEV"."LEAWOOD" 
as
    function post_series_data(in_body CLOB) return varchar2;
    
end leawood;

/
