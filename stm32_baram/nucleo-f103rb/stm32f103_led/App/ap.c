/*
 * ap.c
 *
 *  Created on: Sep 15, 2024
 *      Author: seonghwk
 */

#include "ap.h"

void apInit(void)
{
	ledInit();
}

void apMain(void)
{
	uint32_t pre_time;

	while(1)
	{
		if (millis() - pre_time >= 500)
		{
			pre_time = millis();
			ledToggle(_DEF_CH1);
		}
#if 0
		HAL_GPIO_TogglePin(LED1_GPIO_Port, LED1_Pin);
		HAL_Delay(500);
#endif
	}
}
