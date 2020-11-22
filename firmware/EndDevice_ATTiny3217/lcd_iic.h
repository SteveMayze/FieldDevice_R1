//-----------------------------------------------------
//File: lcd_iic.h
//Auth: ELECTRONIC ASSEMBLY JM
//DATE: 08-07-2012
//-----------------------------------------------------
#ifndef LCDSPI_H
#define LCDSPI_H

#include "mcc_generated_files/mcc.h"
// #define LCD_IIC_SA0_GND 0x78 // 0x 0111 1000 
#define LCD_IIC_SA0_GND 0x3c // 0x 0011 1100 

#define LCD_IIC_SA0_VDD 0x7A
// #define LCD_IIC_SA0_VDD 0x3d // 011 1101

//--- Port definitions ---
#define SDA		p3_4
#define ddSDA	pd3_4
#define SCL		p3_5
#define ddSCL	pd3_5

#define SA0		p3_3
#define ddSA0	pd3_3
#define RES		p6_3
#define ddRES	pd6_3

//--- Standard definitions for LCD ---
#define LCD_HOME_L1	0x80
#define LINE1	0
/*
//HD44780
#define LINE2	LINE1+0x40
#define LINE3	LINE1+0x14
#define	LINE4 	LINE2+0x14
*/
//KS0073/SSD1803(A)
#define LINE2	LINE1+0x20
#define LINE3	LINE1+0x40
#define	LINE4 	LINE1+0x60

#define DISPLAY_ON 	0x04
#define DISPLAY_OFF 0x03
#define CURSOR_ON	0x02
#define CURSOR_OFF	0x05
#define BLINK_ON	0x01
#define BLINK_OFF	0x06


#define TOPVIEW		0x05
#define BOTTOMVIEW	0x06

#define ROMA		0x00
#define ROMB		0x04
#define ROMC		0x0C


void LCD_IIC_initDispl(uint8_t addr);


void WriteChar		(uint8_t character);
void WriteString	(uint8_t * string);
void SetPostion		(uint8_t pos);
void DisplayOnOff	(uint8_t data);
void DefineCharacter(uint8_t postion, uint8_t *data);
void ClrDisplay		(void);
void SetContrast	(uint8_t contr);
void SetView		(uint8_t view);
void SetROM			(uint8_t rom);
#define GETCURSORADDR()	CheckBusy()



#endif