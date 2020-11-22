/* 
 * File:   IS31FL3637.h
 * Author: Steven
 *
 * Created on August 23, 2020, 4:54 PM
 */

#ifndef IS31FL3637_H
#define	IS31FL3637_H

#ifdef	__cplusplus
extern "C" {
#endif


#include "mcc_generated_files/mcc.h" 
    
#define IS31FL3637_Addr7_GND_GND 0x50 //AD1 open (R7 pull-low), ADDR2=GND
#define IS31FL3637_Addr7_GND_VCC 0x53 //AD1 = VIO, ADDR2=GND
#define IS31FL3637_Addr7_GND_SCL 0x51 //AD1 = SCL, ADDR2=GND
#define IS31FL3637_Addr7_GND_SDA 0x52 //AD1 = SDA, ADDR2=GND
    
#define IS31FL3637_Addr8_GND_GND 0xa0 //AD1 open (R7 pull-low), ADDR2=GND
#define IS31FL3637_Addr8_GND_VCC 0xa6 //AD1 = VIO, ADDR2=GND
#define IS31FL3637_Addr8_GND_SCL 0xa2 //AD1 = SCL, ADDR2=GND
#define IS31FL3637_Addr8_GND_SDA 0xa4 //AD1 = SDA, ADDR2=GND
    
#define ROWS 4
#define COLUMNS 8

#define BLUE_LED 0
#define GREEN_LED 1
#define RED_LED 2

#define IS31FL3637_CR 0xFD
#define IS31FL3637_CRWL 0xFE
#define IS31FL3637_INT_MSK_REG 0xF0
#define IS31FL3637_INT_ST_REG 0xF1
    
#define IS31FL3637_LK_TOKEN 0xC5
    
#define IS31FL3637_PAGE_LED_CTRL 0x00
#define IS31FL3637_PAGE_PWM_REG 0x01
#define IS31FL3637_PAGE_ABM_REG 0x02
#define IS31FL3637_PAGE_CFG_REG 0x03



#define ABMCR_3_LTA 0x00
#define ABMCR_3_LTB 0x00
#define ABMCR_3_LB 0x04
#define ABMCR_3_LE 0x06

// PG 3

#define IS31FL3736_CFG     0x00
#define IS31FL3736_GCC     0x01
#define IS31FL3736_ABM_1_1 0x02
#define IS31FL3736_ABM_1_2 0x03
#define IS31FL3736_ABM_1_3 0x04
#define IS31FL3736_ABM_1_4 0x05
#define IS31FL3736_ABM_2_1 0x06
#define IS31FL3736_ABM_2_2 0x07
#define IS31FL3736_ABM_2_3 0x08
#define IS31FL3736_ABM_2_4 0x09
#define IS31FL3736_ABM_3_1 0x0A
#define IS31FL3736_ABM_3_2 0x0B
#define IS31FL3736_ABM_3_3 0x0C
#define IS31FL3736_ABM_3_4 0x0D
#define IS31FL3736_TIME_UPDATE 0x0E

#define ABM_LB_BIT 0x04 // Loop times - Endless

#define ABM_LB_T1 0x00 // Loop begin from T1
#define ABM_LB_T2 0x01 // Loop begin from T2
#define ABM_LB_T3 0x02 // Loop begin from T3
#define ABM_LB_T4 0x03 // Loop begin from T4

#define ABM_LE_BIT 0x06 // Loop times - Endless

#define ABM_LE_T3 0x00 // Loop end from T3 // i.e. off state
#define ABM_LE_T1 0x01 // Loop end from T1 // i.e. on state

#define ABM_LTA_BIT 0x00 // Loop times - Endless

#define ABM_LTA_ENDLESS 0x00 // Loop times - Endless
#define ABM_LTA_1 0x01 // Loop times - 1
#define ABM_LTA_2 0x02 // Loop times - 2
#define ABM_LTA_3 0x03 // Loop times - 3
#define ABM_LTA_4 0x04 // Loop times - 4
#define ABM_LTA_5 0x05 // Loop times - 5
#define ABM_LTA_6 0x06 // Loop times - 6
#define ABM_LTA_7 0x07 // Loop times - 7
#define ABM_LTA_8 0x08 // Loop times - 8
#define ABM_LTA_9 0x09 // Loop times - 9
#define ABM_LTA_10 0x0A // Loop times - 10
#define ABM_LTA_11 0x0B // Loop times - 11
#define ABM_LTA_12 0x0C // Loop times - 12
#define ABM_LTA_13 0x0F // Loop times - 13
#define ABM_LTA_14 0x0E // Loop times - 14
#define ABM_LTA_15 0x0F // Loop times - 15

#define ABM_LTB_BIT 0x00 // Loop times - Endless


#define T1_BITS 0x05
// Register 1 of ABM-x
#define T1_0021 0x00 // 0.21s
#define T1_0042 0x01 // 0.42s
#define T1_0084 0x02 // 0.84s
#define T1_0168 0x03 // 1.68s
#define T1_0336 0x04 // 3.36s
#define T1_0672 0x05 // 6.72s
#define T1_1344 0x06 // 13.44s
#define T1_2688 0x07 // 26.88s

#define T2_BITS 0x01
#define T2_00000 0x00 //0s
#define T2_00021 0x01 // 0.21s
#define T2_00042 0x02 // 0.42s
#define T2_00084 0x03 // 0.84s
#define T2_00168 0x04 // 1.68s
#define T2_00336 0x05 // 3.36s
#define T2_00672 0x06 // 6.72s
#define T2_01344 0x07 // 13.44s
#define T2_02688 0x08 // 26.88s

// Register 2 of ABM-x
#define T3_BITS 0x05
#define T3_0021 0x00 // 0.21s
#define T3_0042 0x01 // 0.42s
#define T3_0084 0x02 // 0.84s
#define T3_0168 0x03 // 1.68s
#define T3_0336 0x04 // 3.36s
#define T3_0672 0x05 // 6.72s
#define T3_1344 0x06 // 13.44s
#define T3_2688 0x07 // 26.88s

#define T4_BITS 0x01
#define T4_00000 0x00 //0s
#define T4_00021 0x01 // 0.21s
#define T4_00042 0x02 // 0.42s
#define T4_00084 0x03 // 0.84s
#define T4_00168 0x04 // 1.68s
#define T4_00336 0x05 // 3.36s
#define T4_00672 0x06 // 6.72s
#define T4_01344 0x07 // 13.44s
#define T4_02688 0x08 // 26.88s
#define T4_05376 0x09 // 53.76s
#define T4_10752 0x0A // 107.52s

    


uint8_t IS31FL3637_pwm_reg[12][16];
uint8_t IS31FL3637_abm_reg[12][16];
uint8_t IS31FL3637_abm_ctl_reg[12];

void IS31FL3637_Initialise_for_rainbow(uint8_t display_addr);
void IS31FL3637_Initialise(uint8_t display_addr);
void IS31FL3637_set_LED(uint8_t display_addr, uint8_t column, uint8_t row, uint8_t red, uint8_t green, uint8_t blue);
void IS31FL3637_update_display(uint8_t display_addr ) ;



#ifdef	__cplusplus
}
#endif

#endif	/* IS31FL3637_H */

