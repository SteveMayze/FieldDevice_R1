--------------------------------------------------------
--  File created - Sunday-February-14-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Package Body COMMON
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE PACKAGE BODY "LEAWOOD_DEV"."COMMON" AS

  PROCEDURE LOG_MESSAGE(module IN varchar2, message in clob) AS
    PRAGMA AUTONOMOUS_TRANSACTION;
  BEGIN
    
    insert into lw_sqllog (created, module, message)
    values (systimestamp, module, message);
    commit;
  END LOG_MESSAGE;

END COMMON;

/
