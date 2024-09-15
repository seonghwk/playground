/*
 * led.h
 *
 *  Created on: Sep 15, 2024
 *      Author: seonghwk
 */

#ifndef INCLUDE_LED_H_
#define INCLUDE_LED_H_

#include "def.h"

bool ledInit(void);
void ledOn(uint8_t ch);
void ledOff(uint8_t ch);
void ledToggle(uint8_t ch);


#endif /* INCLUDE_LED_H_ */
