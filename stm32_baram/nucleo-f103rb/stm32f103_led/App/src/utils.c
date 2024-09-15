/*
 * utils.c
 *
 *  Created on: Sep 15, 2024
 *      Author: seonghwk
 */

#include "utils.h"

void delay(uint32_t time_ms)
{
	HAL_Delay(time_ms);
}

uint32_t millis(void)
{
	return HAL_GetTick();
}
