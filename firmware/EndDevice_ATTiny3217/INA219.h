/* 
 * File:   INA218.h
 * Author: Steven
 *
 * Created on 28 August 2020, 20:36
 */

#ifndef INA219_H
#define	INA219_H

#ifdef	__cplusplus
extern "C" {
#endif

#include "mcc_generated_files/mcc.h" 

#define INA219_RST 15
#define INA219_BRNG 13
#define INA219_PG1 12
#define INA219_PG0 11 
#define INA219_BADC4 10
#define INA219_BADC3 9
#define INA219_BADC2 8
#define INA219_BADC1 7
#define INA219_SADC4 6
#define INA219_SADC3 5
#define INA219_SADC2 4
#define INA219_SADC1 3 
#define INA219_MODE3 2
#define INA219_MODE2 1
#define INA219_MODE1 0
    
#define INA219_BRNG_16 (1 << INA219_BRNG))
    
#define INA219_PG_1 (0 << INA219_PG0)
#define INA219_PG_2 (1 << INA219_PG0)
#define INA219_PG_4 (2 << INA219_PG0)
#define INA219_PG_8 (3 << INA219_PG0)

// BADC / SADC
    
#define INA219_MODE_PWR_DN (0 << INA219_MODE1)
#define INA219_MODE_TRG_SH (1 << INA219_MODE1)
#define INA219_MODE_TRG_B (2 << INA219_MODE1)
#define INA219_MODE_TRG_SHB (3 << INA219_MODE1)
#define INA219_MODE_ADC_OFF (4 << INA219_MODE1)
#define INA219_MODE_CNT_SH (5 << INA219_MODE1)
#define INA219_MODE_CNT_B (6 << INA219_MODE1)
#define INA219_MODE_CNT_SHB (7 << INA219_MODE1)
    
    
#define INA219_CFG (0x00)
#define INA219_SHUNT_VOLTAGE (0x01)
#define INA219_BUS_VOLTAGE (0x02)
#define INA219_POWER (0x03)
#define INA219_CURRENT (0x04)
#define INA219_CAL (0x05)    

//#define INA219_DEFAULT_CFG_LSBFIRST 0x0399
#define INA219_DEFAULT_CFG_LSBFIRST 0x9F21

// #define INA219_DEFAULT_CFG_MSBFIRST 0x9903
#define INA219_DEFAULT_CFG_MSBFIRST 0x9F19
    
#define INA219_ADDR_GND_GND    0b01000000 // Default
#define INA219_ADDR_GND_VS     0b01000001
#define INA219_ADDR_GND_SDA    0b01000010
#define INA219_ADDR_GND_SCL    0b01000011
#define INA219_ADDR_VS_GND     0b01000100
#define INA219_ADDR_VS_VS      0b01000101
#define INA219_ADDR_VS_SDA     0b01000110
#define INA219_ADDR_VS_SCL     0b01000111
#define INA219_ADDR_SDA_GND    0b01001000
#define INA219_ADDR_SDA_VS     0b01001001
#define INA219_ADDR_SDA_SDA    0b01001010
#define INA219_ADDR_SDA_SCL    0b01001011
#define INA219_ADDR_SCL_GND    0b01001100
#define INA219_ADDR_SCL_VS     0b01001101
#define INA219_ADDR_SCL_SDA    0b01001110
#define INA219_ADDR_SCL_SCL    0b01001111
    
    
    struct ina219_data {
        uint16_t raw_shunt_voltage;
        uint16_t raw_bus_voltage;
        uint16_t raw_current;
        uint16_t raw_power;
        
        float shunt_voltage;
        float bus_voltage;
        float power;
        float current;
    };
    
    void INA219_Initialise(uint8_t addr);
    
    struct ina219_data INA219_getReadings();
    
#ifdef	__cplusplus
}
#endif

#endif	/* INA219_H */

