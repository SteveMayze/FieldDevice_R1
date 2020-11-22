//-----------------------------------------------------
//File: lcd_iic.c
//Auth: ELECTRONIC ASSEMBLY JM
//DATE: 08-25-2013
//-----------------------------------------------------

//---Includes---
#include "lcd_iic.h"
#include "TWI0_Util.h"

#include "util/delay.h"

//--- module global variables ---


//Normally you don't need these functions outside this module
static void WriteIns		(uint8_t ins);
static void WriteData		(uint8_t data);

void CheckBusy		(void);


static volatile uint8_t iic_address;



//-----------------------------------------------------
//Func: initDispl()
//Desc: inits Display
//-----------------------------------------------------
void LCD_IIC_initDispl(uint8_t addr) {
    
    iic_address = addr;

	//init Display
	WriteIns(0x3A);	//8-Bit data length extension Bit RE=1; REV=0
	WriteIns(0x09);	//4 line display
	WriteIns(0x06);	//Bottom view
	WriteIns(0x1E);	//Bias setting BS1=1
	WriteIns(0x39);	//8-Bit data length extension Bit RE=0; IS=1
	WriteIns(0x1B);	//BS0=1 -> Bias=1/6
	WriteIns(0x6E); //Divider on and set value
	WriteIns(0x57); //Booster on and set contrast (BB1=C5, DB0=C4)
	WriteIns(0x72); //Set contrast (DB3-DB0=C3-C0)
	WriteIns(0x38); //8-Bit data length extension Bit RE=0; IS=0

	ClrDisplay();
	DisplayOnOff(DISPLAY_ON );
}

//-----------------------------------------------------
//Func: WriteChar(character)
//Desc: sends a single character to display
//-----------------------------------------------------
void WriteChar (uint8_t character)
{
	WriteData(character);
}

//-----------------------------------------------------
//Func: WriteString(string)
//Desc: sends a string to display, must be 0 terminated
//-----------------------------------------------------
void WriteString(uint8_t * string)
{
	do
	{
		WriteData(*string++);
	}
	while(*string);
}


//-----------------------------------------------------
//Func: SetPostion(postion)
//Desc: set postion
//-----------------------------------------------------
void SetPostion(uint8_t pos)
{
	WriteIns(LCD_HOME_L1+pos);
}

//-----------------------------------------------------
//Func: DisplayOnOff(control)
//Desc: use definitions of header file to set display
//-----------------------------------------------------
void DisplayOnOff(uint8_t data)
{
	WriteIns(0x08+data);
}

//-----------------------------------------------------
//Func: DefineCharacter(memory postion, character data)
//Desc: stores an own defined character
//-----------------------------------------------------
void DefineCharacter(uint8_t postion, uint8_t *data)
{
	unsigned char i=0;
	WriteIns(0x40+8*postion);

	for (i=0; i<8; i++)
	{
		WriteData(data[i]);
	}
	SetPostion(LINE1);
}
//-----------------------------------------------------
//Func: ClrDisplay
//Desc: Clears entire Display content and set home pos
//-----------------------------------------------------
void ClrDisplay(void)
{
	WriteIns(0x01);
	SetPostion(LINE1);
}

//-----------------------------------------------------
//Func: SetContrast
//Desc: Sets contrast 0..63
//-----------------------------------------------------
void SetContrast(uint8_t contr)
{
	WriteIns(0x39);
	WriteIns(0x54 | (contr >> 4));
	WriteIns(0x70 | (contr & 0x0F));
	WriteIns(0x38);

}

//-----------------------------------------------------
//Func: SetView
//Desc: view bottom view(0x06), top view (0x05)
//-----------------------------------------------------
void SetView(unsigned char view)
{
	WriteIns(0x3A);
	WriteIns(view);
	WriteIns(0x38);
}

//-----------------------------------------------------
//Func: SetROM
//Desc: Changes the Rom code (ROMA=0x00, ROMB=0x04, ROMC=0x0C)
//---------------------------------------------------
void SetROM (uint8_t rom)
{
	WriteIns(0x2A);
	WriteIns(0x72);
	WriteData(rom);
	WriteIns(0x28);
}

//-----------------------------------------------------
//Func: WriteIns(instruction)
//Desc: sends instruction to display
//-----------------------------------------------------
static void WriteIns(uint8_t ins)
{
	CheckBusy();
	TWI0_write1ByteRegister(iic_address, 0x80, ins); //Control byte C0=0 & D/C = 0)

}

//-----------------------------------------------------
//Func: WriteData(data)
//Desc: sends data to display
//-----------------------------------------------------
static void WriteData(uint8_t data)
{
	CheckBusy();
	TWI0_write1ByteRegister(iic_address, 0x40, data); //Control byte C0=0 & D/C = 1)
}

//-----------------------------------------------------
//Func: CheckBusy()
//Desc: checks if display is idle
//-----------------------------------------------------
void CheckBusy(void)
{
	while(TWI0_read1ByteRegister(iic_address, 0x80) & 0x80);  //check busyFlag
    ;
}

