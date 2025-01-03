#ifndef _SDK_CONFIG_H_
#define _SDK_CONFIG_H_

#include <api_hal_uart.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct
{
    bool enable_fota;
    bool enable_log_dispach;
    UART_Port_t io_interface;
    uint32_t user_app_start_delay_ms;
    uint16_t user_app_StackSize;
    
} SDK_Config_t;

extern SDK_Config_t sdkConfig;

#endif // _sdkConfig_H_
