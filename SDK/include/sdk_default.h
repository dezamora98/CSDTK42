#ifndef SDK_DEFAULT_H
#define SDK_DEFAULT_H

#include <sdk_config.h>

#ifndef IO_INTERFACE
#define IO_INTERFACE 0
#endif // !IO_INTERFACE  default value
#ifndef DEBUG_LOG_ENABLE
#define DEBUG_LOG_ENABLE 0
#endif // !DEBUG_LOG_ENABLE default value

// User application start delay in milliseconds
#ifndef USER_APP_START_MS
#define USER_APP_START_MS 5000
#endif // !USER_APP_START_MS  default value

// User application stack size in bytes
#ifndef USER_APP_STACK_SIZE
#define USER_APP_STACK_SIZE 2048
#endif // !USER_APP_STACK_SIZE  default value

// UART I/O configuration
#ifndef UART_IO_CONFIG
#define UART_IO_CONFIG                     \
    (UART_Config_t)                        \
    {                                      \
        .baudRate = UART_BAUD_RATE_115200, \
        .dataBits = UART_DATA_BITS_8,      \
        .errorCallback = NULL,             \
        .parity = UART_PARITY_NONE,        \
        .stopBits = UART_STOP_BITS_1,      \
        .useEvent = false,                 \
    }
#endif // UART_IO_CONFIG  default value

// Firmware Over-the-Air (FOTA) enable settings:
#ifndef ENABLE_UART_FOTA
#define ENABLE_UART_FOTA 0
#endif // !ENABLE_UART_FOTA  default value

// Default UART configuration for FOTA
#ifndef DEFAULT_FOTA_UART_CONFIG
#define DEFAULT_FOTA_UART_CONFIG           \
    (UART_Config_t)                        \
    {                                      \
        .baudRate = UART_BAUD_RATE_115200, \
        .dataBits = UART_DATA_BITS_8,      \
        .stopBits = UART_STOP_BITS_1,      \
        .parity = UART_PARITY_NONE,        \
        .rxCallback = NULL,                \
        .useEvent = true,                  \
    }
#endif // DEFAULT_FOTA_UART_CONFIG  default value



#endif // SDK_DEFAULT_H