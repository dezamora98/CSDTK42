#ifndef _SDK_CONFIG_H_
#define _SDK_CONFIG_H_

#include <api_hal_uart.h>
#include <stdint.h>
#include <stdbool.h>

// I/O Interface selection:
// 0 - TRACE: Use the trace interface for I/O
// 1 - UART1: Use UART1 interface for I/O
// 2 - UART2: Use UART2 interface for I/O
#define IO_INTERFACE 0

// UART I/O configuration
// This macro initializes a UART_Config_t structure with specific settings for UART I/O
#define UART_IO_CONFIG                 \
  (UART_Config_t)                      \
  {                                    \
    .baudRate = UART_BAUD_RATE_115200, \
    .dataBits = UART_DATA_BITS_8,      \
    .errorCallback = NULL,             \
    .parity = UART_PARITY_NONE,        \
    .stopBits = UART_STOP_BITS_1,      \
    .useEvent = false,                 \
  }

// Firmware Over-the-Air (FOTA) enable settings:
// 0 - Disabled: FOTA is not enabled
// 1 - UART1: FOTA through UART1
// 2 - UART2: FOTA through UART2
#define ENABLE_UART_FOTA  0

// Default UART configuration for FOTA
// This macro initializes a UART_Config_t structure with default settings for FOTA
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

// Debug logging enable settings:
// 0 - Disabled: Debug logging is not enabled
// 1 - Enabled: Debug logging is enabled
#define DEBUG_LOG_ENABLE  1

// User application start delay in milliseconds
// Defines the delay time before the user application starts
#define USER_APP_START_MS  5000

// User application stack size in bytes
// Defines the stack size allocated for the user application
#define USER_APP_STACK_SIZE  2048

#endif // _SDK_CONFIG_H_
