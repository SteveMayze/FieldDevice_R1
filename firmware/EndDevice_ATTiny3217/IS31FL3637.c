
#include "TWI0_Util.h"
#include "IS31FL3637.h"


uint8_t IS31FL3637_raddr = 0;
uint8_t IS31FL3637_caddr = 0;


void IS31FL3637_set_page(uint8_t display_addr, uint8_t page) {
    TWI0_write1ByteRegister(display_addr, IS31FL3637_CRWL, IS31FL3637_LK_TOKEN);
    TWI0_write1ByteRegister(display_addr, IS31FL3637_CR, page); // Turn to page 0: LED Control    
}



void by_rows() {
  for ( uint8_t row = 0; row < ROWS; row++) {
    for( uint8_t column = 0; column < COLUMNS; column++){
      IS31FL3637_raddr = row*3;
      IS31FL3637_caddr = column *2;
      switch(row){
        case 0:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x03;
        break;
        case 1:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x01;
        break;
        case 2:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x02;
        break;
        case 3:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x03;
        break;
      }
    }
  }

}

void by_columns(){
  for ( uint8_t row = 0; row < ROWS; row++) {
    for( uint8_t column = 0; column < COLUMNS; column++){
      IS31FL3637_raddr = row*3;
      IS31FL3637_caddr = column *2;

      switch(column){
        case 0:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x03;
        break;
        case 1:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x01;
        break;
        case 2:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x02;
        break;
        case 3:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x03;
        break;
        case 4:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x01;
        break;
        case 5:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x02;
        break;
        case 6:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x01;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x03;
        break;
        case 7:
        IS31FL3637_abm_reg[IS31FL3637_raddr + RED_LED][IS31FL3637_caddr] = 0x02;
        IS31FL3637_abm_reg[IS31FL3637_raddr + GREEN_LED][IS31FL3637_caddr] = 0x03;
        IS31FL3637_abm_reg[IS31FL3637_raddr + BLUE_LED][IS31FL3637_caddr] = 0x01;
        break;
      }
    }
  }

}

void IS31FL3637_Initialise(uint8_t display_addr) {
    
    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_CFG_REG);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_CFG, 0x00);

    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_LED_CTRL);
    for (uint8_t i = 0; i < 0x18; i++) {
        TWI0_write1ByteRegister(display_addr, i, 0xFF); // enable all LEDs
    }
    // uint8_t IS31FL3637_pwm_reg[12][16]; Rows 12/2 columns 16/2

    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_PWM_REG);
    for (uint8_t i = 0; i < 192; i++) {
        TWI0_write1ByteRegister(display_addr, i, 0x7F); //Set PWM data to 0
    }


    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_CFG_REG); //Turn to page 3: function registers
    TWI0_write1ByteRegister(display_addr, IS31FL3736_GCC, 0x1f); //global current
    TWI0_write1ByteRegister(display_addr, IS31FL3736_CFG, 0x01); //Release software shutdown to normal operation
    TWI0_write1ByteRegister(display_addr, IS31FL3736_TIME_UPDATE, 0x00);

}

void IS31FL3637_set_LED(uint8_t display_addr, uint8_t column, uint8_t row, uint8_t red, uint8_t green, uint8_t blue) {
    
    uint8_t caddr = column * 2;
    uint8_t raddr = row * 3;

    IS31FL3637_pwm_reg[raddr + RED_LED][caddr] = red;
    IS31FL3637_pwm_reg[raddr + GREEN_LED][caddr] = green;
    IS31FL3637_pwm_reg[raddr + BLUE_LED][caddr] = blue;
    
}

void IS31FL3637_update_display(uint8_t display_addr ) {
    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_PWM_REG);
    uint8_t pwmAddr = 0;
    for (uint8_t i = 0; i < 12; i++) {
        for (uint8_t j = 0; j < 16; j = j + 2) {
            TWI0_write1ByteRegister(display_addr, pwmAddr, IS31FL3637_pwm_reg[i][j]); //Set PWM data to 0
            pwmAddr = pwmAddr + 2;
        }
    }    
}

void IS31FL3637_Initialise_for_rainbow(uint8_t display_addr) {
    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_LED_CTRL);
    for (uint8_t i = 0; i < 0x18; i++) {
        TWI0_write1ByteRegister(display_addr, i, 0xFF); // enable all LEDs
    }

    by_columns();

    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_ABM_REG);
    uint8_t pwmAddr = 0;
    for (uint8_t i = 0; i < 12; i++) {
        for (uint8_t j = 0; j < 16; j = j + 2) {
            TWI0_write1ByteRegister(display_addr, pwmAddr, IS31FL3637_abm_reg[i][j]); //Set PWM data to 0
            pwmAddr = pwmAddr + 2;
        }
    }

    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_CFG_REG);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_CFG, 0x00);

    uint8_t timing_1 = T1_0042 << T1_BITS | T2_00000 << T2_BITS;
    uint8_t timing_2 = T3_0042 << T3_BITS | T4_00042 << T4_BITS;
    //uint8_t timing_3 = T1_0021 << T1_BITS | T2_00000 << T2_BITS;
    //uint8_t timing_4 = T3_0021 << T3_BITS | T4_00021 << T4_BITS;
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_1_1, timing_1);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_1_2, timing_2);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_1_3, ABM_LE_T3 << ABM_LE_BIT | ABM_LB_T2 << ABM_LB_BIT | ABM_LTA_ENDLESS << ABM_LTA_BIT);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_1_4, 0b00000000);

    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_2_1, timing_1);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_2_2, timing_2);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_2_3, ABM_LE_T3 << ABM_LE_BIT | ABM_LB_T1 << ABM_LB_BIT | ABM_LTA_ENDLESS << ABM_LTA_BIT);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_2_4, 0b00000000);

    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_3_1, timing_1);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_3_2, timing_2);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_3_3, ABM_LE_T3 << ABM_LE_BIT | ABM_LB_T4 << ABM_LB_BIT | ABM_LTA_ENDLESS << ABM_LTA_BIT);
    TWI0_write1ByteRegister(display_addr, IS31FL3736_ABM_3_4, 0b00000000);

    //can use buffer write type as figure 7 in data sheet
    IS31FL3637_set_page(display_addr, IS31FL3637_PAGE_CFG_REG); //Turn to page 3: function registers
    TWI0_write1ByteRegister(display_addr, IS31FL3736_GCC, 0x1f); //global current
    TWI0_write1ByteRegister(display_addr, IS31FL3736_CFG, 0x03); //Release software shutdown to normal operation
    TWI0_write1ByteRegister(display_addr, IS31FL3736_TIME_UPDATE, 0x00);

}