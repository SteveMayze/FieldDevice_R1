
#include "INA219.h"
#include "TWI0_Util.h"
#include "util/delay.h"

static volatile uint8_t iic_address;
uint8_t ina219_buf[3];

// #define CAL_MSBFIRST 0x0010
#define CAL_MSBFIRST 0x0E0F

void INA219_Initialise(uint8_t addr) {
    iic_address = addr;

    TWI0_write2ByteRegister(iic_address, INA219_CAL, CAL_MSBFIRST);
    TWI0_write2ByteRegister(iic_address, INA219_CFG, INA219_DEFAULT_CFG_MSBFIRST);
}

uint16_t get_shunt_voltage_raw() {
    uint16_t result = TWI0_read2ByteRegister(iic_address, INA219_SHUNT_VOLTAGE);
    return result;
}

uint16_t get_bus_voltage_raw() {
    uint16_t reading = TWI0_read2ByteRegister(iic_address, INA219_BUS_VOLTAGE);
    return reading;
}

uint16_t get_current_raw() {
    TWI0_write2ByteRegister(iic_address, INA219_CAL, CAL_MSBFIRST);
    return TWI0_read2ByteRegister(iic_address, INA219_CURRENT);

}

uint16_t get_power_raw() {
    TWI0_write2ByteRegister(iic_address, INA219_CAL, CAL_MSBFIRST);
    return TWI0_read2ByteRegister(iic_address, INA219_POWER);

}

struct ina219_data INA219_getReadings() {

    struct ina219_data readings;

    // TWI0_write2ByteRegister(iic_address, INA219_CAL, CAL_MSBFIRST);
    // TWI0_write2ByteRegister(iic_address, INA219_CFG, INA219_DEFAULT_CFG_MSBFIRST);

    // uint16_t reading;
    readings.bus_voltage = 0.0;
    readings.shunt_voltage = 0.0;
    readings.current = 0.0;
    readings.power = 0.0;

    bool reading_ok = false;
    while (!reading_ok) {
        readings.raw_bus_voltage = get_bus_voltage_raw();
        reading_ok = readings.raw_bus_voltage & 0x02;
        _delay_ms(500);
    }
    readings.bus_voltage = (int16_t) ((readings.raw_bus_voltage >> 3) * 4);
    readings.bus_voltage = readings.bus_voltage * 0.001;

    readings.raw_shunt_voltage = get_shunt_voltage_raw();
    readings.shunt_voltage = readings.raw_shunt_voltage * 0.01;


    readings.raw_current = get_current_raw();
    readings.current = ((float) readings.raw_current / 10.0);

    readings.raw_power = get_power_raw();
    readings.power = ((float) readings.raw_power * 2.0);


    return readings;

}

