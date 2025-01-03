#ifndef __API_DEBUG_H_
#define __API_DEBUG_H_

#include "sdk_init.h"
#include "sdk_config.h"
#include "api_inc_uart.h"
#include "api_hal_uart.h"

#define DEFAULT_UART_CONFIG            \
  (UART_Config_t)                      \
  {                                    \
    .baudRate = UART_BAUD_RATE_115200, \
    .dataBits = UART_DATA_BITS_8,      \
    .errorCallback = NULL,             \
    .parity = UART_PARITY_NONE,        \
    .stopBits = UART_STOP_BITS_1,      \
    .useEvent = false,                 \
  }

/**
 * @brief bool Trace(uint16_t nIndex,PCSTR fmt, ...)
 *   send debug infomation to tracer of coolwatcher
 * @param      nIndex: trace level( cool watcher will print level as `MMI nIndex`)
 * @param      fmt: format string eg:"test integet:%d"
 * @param      ...: parameters
 * @attention not support float(%f) yet! can use `gcvt()` convert to string firstly
 */
#define Trace CSDK_FUNC(Trace)

#define MEMBLOCK_Trace CSDK_FUNC(MEMBLOCK_Trace)

/**
 * @brief Function to trace memory block
 *
 * @param nIndex Trace level
 * @param buffer Buffer to trace
 * @param len Length of the buffer
 * @param radix Radix for formatting
 */
void Trace_MemBlock(uint16_t nIndex, uint8_t *buffer, uint16_t len, uint8_t radix);

/**
 * @brief set print debug information to interface port selected
 */
void setIOInterface();

/**
 * @brief Print user information to UART port selected in "EnableUartDebug(uartDebugPort)"
 * @param format Format string
 * @param ... Additional arguments
 */
void uPrintf(const char *format, ...);

/**
 * @brief Print user information to Trace interface "(MMI1)"
 * @param format Format string
 * @param ... Additional arguments
 */
#define tPrintf(format, ...) Trace(1, format, ##__VA_ARGS__)

/**
 * @brief Macro for printing debug information with file and line info
 *
 * @param format Format string
 * @param ... Additional arguments
 */
#define uDebug(format, ...) \
  uPrintf("%s:%d: " format "\n\r", __FILE__, __LINE__, ##__VA_ARGS__)

/**
 * @brief Print debug information to Trace interface "(MMI1)"
 * @param format Format string
 * @param ... Additional arguments
 */
#define tDebug(format, ...) Trace(1, "%s:%d: " format "\n\r", __FILE__, __LINE__, ##__VA_ARGS__)

/**
 * @brief Macro for printing debug information based on UART I/O state
 * @param format Format string
 * @param ... Additional arguments
 */
#define debug(format, ...)                \
  {                                       \
    if (sdkConfig.io_interface != TRACE) \
      uDebug(format, ##__VA_ARGS__);      \
    else                                  \
      tDebug(format, ##__VA_ARGS__);      \
  }

#define LIBS_DEBUG_I 15
#define LIBS_DEBUG_E 16

#endif