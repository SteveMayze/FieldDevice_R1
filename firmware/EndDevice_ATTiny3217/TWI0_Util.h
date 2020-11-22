/* 
 * File:   TW0_Util.h
 * Author: Steven
 *
 * Created on August 23, 2020, 5:21 PM
 */

#ifndef TW0_UTIL_H
#define	TW0_UTIL_H

#ifdef	__cplusplus
extern "C" {
#endif

#include "mcc_generated_files/include/twi0_master.h"

void TWI0_write1ByteRegister(twi0_address_t address, uint8_t reg, uint8_t data);

void TWI0_write2ByteRegister(twi0_address_t address, uint8_t reg, uint16_t data);

void TWI0_writeNBytes(twi0_address_t address, void* data, size_t len);

uint8_t TWI0_read1ByteRegister(twi0_address_t address, uint8_t reg);

uint16_t TWI0_read2ByteRegister(twi0_address_t address, uint8_t reg);

#ifdef	__cplusplus
}
#endif

#endif	/* TW0_UTIL_H */

