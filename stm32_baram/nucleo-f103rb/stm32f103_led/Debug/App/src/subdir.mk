################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../App/src/led.c \
../App/src/utils.c 

OBJS += \
./App/src/led.o \
./App/src/utils.o 

C_DEPS += \
./App/src/led.d \
./App/src/utils.d 


# Each subdirectory must supply rules for building sources it contributes
App/src/%.o App/src/%.su App/src/%.cyclo: ../App/src/%.c App/src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F103xB -c -I../Core/Inc -I../Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -I../Drivers/STM32F1xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32F1xx/Include -I../Drivers/CMSIS/Include -I"/Users/seonghwk/Documents/02_Areas/playground/stm32_baram/nucleo-f103rb/stm32f103_led/App" -I"/Users/seonghwk/Documents/02_Areas/playground/stm32_baram/nucleo-f103rb/stm32f103_led/App/include" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-App-2f-src

clean-App-2f-src:
	-$(RM) ./App/src/led.cyclo ./App/src/led.d ./App/src/led.o ./App/src/led.su ./App/src/utils.cyclo ./App/src/utils.d ./App/src/utils.o ./App/src/utils.su

.PHONY: clean-App-2f-src

