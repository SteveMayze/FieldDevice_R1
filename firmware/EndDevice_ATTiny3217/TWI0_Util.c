

#include "TWI0_Util.h"



static twi0_operations_t wr1RegCompleteHandler_example(void *ptr)
{
    I2C0_SetBuffer(ptr,1);
    I2C0_SetDataCompleteCallback(NULL,NULL);
    return I2C0_CONTINUE;
}

void TWI0_write1ByteRegister(twi0_address_t address, uint8_t reg, uint8_t data)
{
    while(!I2C0_Open(address)); // sit here until we get the bus..
    I2C0_SetDataCompleteCallback(wr1RegCompleteHandler_example,&data);
    I2C0_SetBuffer(&reg, 1);
    I2C0_SetAddressNackCallback(I2C0_SetRestartWriteCallback, NULL); //NACK polling?
    I2C0_MasterWrite();
    while(I2C0_BUSY == I2C0_Close()); // sit here until finished.
}


void TWI0_writeNBytes(twi0_address_t address, void* data, size_t len)
{
    while(!I2C0_Open(address)); // sit here until we get the bus..
    I2C0_SetBuffer(data, len);
    I2C0_SetAddressNackCallback(I2C0_SetRestartWriteCallback, NULL); //NACK polling?
    I2C0_MasterWrite();
    while(I2C0_BUSY == I2C0_Close()); // sit here until finished.
}


static twi0_operations_t wr2RegCompleteHandler_example(void *ptr)
{
    I2C0_SetBuffer(ptr,2);
    I2C0_SetDataCompleteCallback(NULL,NULL);
    return I2C0_CONTINUE;
}

void TWI0_write2ByteRegister(twi0_address_t address, uint8_t reg, uint16_t data)
{
    while(!I2C0_Open(address)); // sit here until we get the bus..
    I2C0_SetDataCompleteCallback(wr2RegCompleteHandler_example,&data);
    I2C0_SetBuffer(&reg,1);
    I2C0_SetAddressNackCallback(I2C0_SetRestartWriteCallback,NULL); //NACK polling?
    I2C0_MasterWrite();
    while(I2C0_BUSY == I2C0_Close()); // sit here until finished.
}


/****************************************************************/


static twi0_operations_t rd1RegCompleteHandler(void *ptr)
{
    I2C0_SetBuffer(ptr,1);
    I2C0_SetDataCompleteCallback(NULL,NULL);
    return I2C0_RESTART_READ;
}

uint8_t TWI0_read1ByteRegister(twi0_address_t address, uint8_t reg)
{
    uint8_t    d2=42;
    twi0_error_t e;
    int x;

    for(x = 2; x != 0; x--)
    {
        while(!I2C0_Open(address)); // sit here until we get the bus..
        I2C0_SetDataCompleteCallback(rd1RegCompleteHandler,&d2);
        I2C0_SetBuffer(&reg, 1);
        I2C0_SetAddressNackCallback(I2C0_SetRestartWriteCallback, NULL); //NACK polling?
        I2C0_MasterWrite();
        while(I2C0_BUSY == (e = I2C0_Close())); // sit here until finished.
        if(e==I2C0_NOERR) break;
    }
    

    return d2;
}

static twi0_operations_t rd2RegCompleteHandler(void *ptr)
{
    I2C0_SetBuffer(ptr,2);
    I2C0_SetDataCompleteCallback(NULL,NULL);
    return I2C0_RESTART_READ;
}

uint16_t TWI0_read2ByteRegister(twi0_address_t address, uint8_t reg)
{
    // result is little endian
    uint16_t    result;

    while(!I2C0_Open(address)); // sit here until we get the bus..
    I2C0_SetDataCompleteCallback(rd2RegCompleteHandler, &result);
    I2C0_SetBuffer(&reg, 1);
    I2C0_SetAddressNackCallback(I2C0_SetRestartWriteCallback, NULL); //NACK polling?
    I2C0_MasterWrite();
    while(I2C0_BUSY == I2C0_Close()); // sit here until finished.
    
    return (result << 8 | result >> 8);
}
