/**
  @Company
    Microchip Technology Inc.

  @Description
    This Source file provides APIs.
    Generation Information :
    Driver Version    :   1.0.0
*/
/*
    (c) 2018 Microchip Technology Inc. and its subsidiaries. 
    
    Subject to your compliance with these terms, you may use Microchip software and any 
    derivatives exclusively with Microchip products. It is your responsibility to comply with third party 
    license terms applicable to your use of third party software (including open source software) that 
    may accompany Microchip software.
    
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY 
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS 
    FOR A PARTICULAR PURPOSE.
    
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP 
    HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO 
    THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL 
    CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT 
    OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS 
    SOFTWARE.
*/


#include "../include/pin_manager.h"
static void (*PORTB_PB3_InterruptHandler)(void);
static void (*PORTB_PB2_InterruptHandler)(void);
static void (*PORTB_SW300_PB5_InterruptHandler)(void);
static void (*PORTB_LED_InterruptHandler)(void);
static void (*PORTA_SW1_PA6_InterruptHandler)(void);
static void (*PORTB_PB1_InterruptHandler)(void);
static void (*PORTB_PB0_InterruptHandler)(void);

void PORT_Initialize(void);

void PIN_MANAGER_Initialize()
{
    PORT_Initialize();

    /* DIR Registers Initialization */
    PORTA.DIR = 0x00;
    PORTB.DIR = 0x14;
    PORTC.DIR = 0x00;

    /* OUT Registers Initialization */
    PORTA.OUT = 0x00;
    PORTB.OUT = 0x00;
    PORTC.OUT = 0x00;

    /* PINxCTRL registers Initialization */
    PORTA.PIN0CTRL = 0x00;
    PORTA.PIN1CTRL = 0x00;
    PORTA.PIN2CTRL = 0x00;
    PORTA.PIN3CTRL = 0x00;
    PORTA.PIN4CTRL = 0x00;
    PORTA.PIN5CTRL = 0x00;
    PORTA.PIN6CTRL = 0x01;
    PORTA.PIN7CTRL = 0x01;
    PORTB.PIN0CTRL = 0x00;
    PORTB.PIN1CTRL = 0x00;
    PORTB.PIN2CTRL = 0x00;
    PORTB.PIN3CTRL = 0x00;
    PORTB.PIN4CTRL = 0x00;
    PORTB.PIN5CTRL = 0x01;
    PORTB.PIN6CTRL = 0x00;
    PORTB.PIN7CTRL = 0x00;
    PORTC.PIN0CTRL = 0x00;
    PORTC.PIN1CTRL = 0x00;
    PORTC.PIN2CTRL = 0x00;
    PORTC.PIN3CTRL = 0x00;
    PORTC.PIN4CTRL = 0x00;
    PORTC.PIN5CTRL = 0x00;
    PORTC.PIN6CTRL = 0x00;
    PORTC.PIN7CTRL = 0x00;

    /* PORTMUX Initialization */
    PORTMUX.CTRLA = 0x00;
    PORTMUX.CTRLB = 0x00;
    PORTMUX.CTRLC = 0x00;
    PORTMUX.CTRLD = 0x00;

    // register default ISC callback functions at runtime; use these methods to register a custom function
    PORTB_PB3_SetInterruptHandler(PORTB_PB3_DefaultInterruptHandler);
    PORTB_PB2_SetInterruptHandler(PORTB_PB2_DefaultInterruptHandler);
    PORTB_SW300_PB5_SetInterruptHandler(PORTB_SW300_PB5_DefaultInterruptHandler);
    PORTB_LED_SetInterruptHandler(PORTB_LED_DefaultInterruptHandler);
    PORTA_SW1_PA6_SetInterruptHandler(PORTA_SW1_PA6_DefaultInterruptHandler);
    PORTB_PB1_SetInterruptHandler(PORTB_PB1_DefaultInterruptHandler);
    PORTB_PB0_SetInterruptHandler(PORTB_PB0_DefaultInterruptHandler);
}

void PORT_Initialize(void)
{
    /* On AVR devices all peripherals are enable from power on reset, this
     * disables all peripherals to save power. Driver shall enable
     * peripheral if used */

    /* Set all pins to low power mode */
    for (uint8_t i = 0; i < 8; i++) {
        *((uint8_t *)&PORTA + 0x10 + i) |= 1 << PORT_PULLUPEN_bp;
    }
    
    for (uint8_t i = 0; i < 8; i++) {
        *((uint8_t *)&PORTB + 0x10 + i) |= 1 << PORT_PULLUPEN_bp;
    }
    
    for (uint8_t i = 0; i < 8; i++) {
        *((uint8_t *)&PORTC + 0x10 + i) |= 1 << PORT_PULLUPEN_bp;
    }
    
}

/**
  Allows selecting an interrupt handler for PORTB_PB3 at application runtime
*/
void PORTB_PB3_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_PB3_InterruptHandler = interruptHandler;
}

void PORTB_PB3_DefaultInterruptHandler(void)
{
    // add your PORTB_PB3 interrupt custom code
    // or set custom function using PORTB_PB3_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTB_PB2 at application runtime
*/
void PORTB_PB2_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_PB2_InterruptHandler = interruptHandler;
}

void PORTB_PB2_DefaultInterruptHandler(void)
{
    // add your PORTB_PB2 interrupt custom code
    // or set custom function using PORTB_PB2_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTB_SW300_PB5 at application runtime
*/
void PORTB_SW300_PB5_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_SW300_PB5_InterruptHandler = interruptHandler;
}

void PORTB_SW300_PB5_DefaultInterruptHandler(void)
{
    // add your PORTB_SW300_PB5 interrupt custom code
    // or set custom function using PORTB_SW300_PB5_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTB_LED at application runtime
*/
void PORTB_LED_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_LED_InterruptHandler = interruptHandler;
}

void PORTB_LED_DefaultInterruptHandler(void)
{
    // add your PORTB_LED interrupt custom code
    // or set custom function using PORTB_LED_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTA_SW1_PA6 at application runtime
*/
void PORTA_SW1_PA6_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTA_SW1_PA6_InterruptHandler = interruptHandler;
}

void PORTA_SW1_PA6_DefaultInterruptHandler(void)
{
    // add your PORTA_SW1_PA6 interrupt custom code
    // or set custom function using PORTA_SW1_PA6_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTB_PB1 at application runtime
*/
void PORTB_PB1_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_PB1_InterruptHandler = interruptHandler;
}

void PORTB_PB1_DefaultInterruptHandler(void)
{
    // add your PORTB_PB1 interrupt custom code
    // or set custom function using PORTB_PB1_SetInterruptHandler()
}
/**
  Allows selecting an interrupt handler for PORTB_PB0 at application runtime
*/
void PORTB_PB0_SetInterruptHandler(void (* interruptHandler)(void)) 
{
    PORTB_PB0_InterruptHandler = interruptHandler;
}

void PORTB_PB0_DefaultInterruptHandler(void)
{
    // add your PORTB_PB0 interrupt custom code
    // or set custom function using PORTB_PB0_SetInterruptHandler()
}
ISR(PORTA_PORT_vect)
{  
    // Call the interrupt handler for the callback registered at runtime
    if(VPORTA.INTFLAGS & PORT_INT6_bm)
    {
       PORTA_SW1_PA6_InterruptHandler();
    }

    /* Clear interrupt flags */
    VPORTA.INTFLAGS = 0xff;
}

ISR(PORTB_PORT_vect)
{  
    // Call the interrupt handler for the callback registered at runtime
    if(VPORTB.INTFLAGS & PORT_INT3_bm)
    {
       PORTB_PB3_InterruptHandler();
    }
    if(VPORTB.INTFLAGS & PORT_INT2_bm)
    {
       PORTB_PB2_InterruptHandler();
    }
    if(VPORTB.INTFLAGS & PORT_INT5_bm)
    {
       PORTB_SW300_PB5_InterruptHandler();
    }
    if(VPORTB.INTFLAGS & PORT_INT4_bm)
    {
       PORTB_LED_InterruptHandler();
    }
    if(VPORTB.INTFLAGS & PORT_INT1_bm)
    {
       PORTB_PB1_InterruptHandler();
    }
    if(VPORTB.INTFLAGS & PORT_INT0_bm)
    {
       PORTB_PB0_InterruptHandler();
    }

    /* Clear interrupt flags */
    VPORTB.INTFLAGS = 0xff;
}

