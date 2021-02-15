--------------------------------------------------------
--  File created - Sunday-February-14-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Package COMMON
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE PACKAGE "LEAWOOD_DEV"."COMMON" AS 

  /* TODO enter package declarations (types, exceptions, methods etc) here */ 
  PROCEDURE LOG_MESSAGE(module IN varchar2, message in clob);

END COMMON;

/
