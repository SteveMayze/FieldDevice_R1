--------------------------------------------------------
--  File created - Sunday-February-14-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Package Body LEAWOOD
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE PACKAGE BODY "LEAWOOD_DEV"."LEAWOOD" 
as
    function post_series_data(in_body CLOB) return varchar2
    as
        module_name CONSTANT VARCHAR2(128) := 'post_series_data';
        l_json           json_object_t;
    
        l_devId VARCHAR2(64);
        l_address VARCHAR2(64);
        l_defId VARCHAR2(64);
        l_label VARCHAR2(64);
        l_value NUMBER;
        l_code  NUMBER;
        l_errm  VARCHAR2(1000);
        
        l_domain lw_device.domain%type;
        l_class lw_device.class%type;

        response VARCHAR2(4000);
        
    begin
        common.log_message(module_name, 'BEGIN');
        l_json := json_object_t.parse( in_body );
        l_address := l_json.get_string('address');
        l_label := l_json.get_string('label');
        l_value := l_json.get_number('value');
        
        common.log_message(module_name, 'Getting device with addess: '||l_address);
        select device_id, domain, class into l_devId, l_domain, l_class
        from LW_DEVICE
        where serial_id = l_address;
        common.log_message(module_name, 'Found device id: '||l_address);

        common.log_message(module_name, 'Getting data def with label: '||l_devId);
        select def_id into l_defId
        from lw_data_def
        where label = l_label
          and domain = l_domain 
          and class = l_class;
        common.log_message(module_name, 'Found data def id: '||l_defId);

        insert into lw_data_series data
            (DEVICE_ID, DEF_ID, POINT_TIMESTAMP, POINT_VALUE)
        values (
            l_devId, l_defId, systimestamp, l_value
        );
    
        response := '{"response": "OK", "device_id": "'|| 
            l_devId ||
            '", "data_def": "'|| 
            l_defId||
            '", value: '||
            to_char(l_value)||
            '}';
            common.log_message(module_name, 'END '||response);
        COMMIT;
        return response;
    EXCEPTION
      WHEN OTHERS THEN
        l_code := SQLCODE;
        l_errm := SQLERRM;
        ROLLBACK;
        response := '{"response": "FAIL", "sql-code": "'||l_code||'", "sql-error":"'||l_errm||'"}';
        common.log_message(module_name, 'END'||response);
       return response;
    end post_series_data;
end leawood;

/
