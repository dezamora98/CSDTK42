#ifndef __API_DEBUG_H_
#define __API_DEBUG_H_

#include "sdk_init.h"
#include "sdk_default.h"
#include "api_inc_uart.h"
#include "api_hal_uart.h"

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
 * @brief Print user information to Trace interface "(MMI1)"
 * @param format Format string
 * @param ... Additional arguments
 */
#define tPrintf(format, ...) Trace(1, format, ##__VA_ARGS__)

/**
 * @brief Print debug information to Trace interface "(MMI1)"
 * @param format Format string
 * @param ... Additional arguments
 */
#define tDebug(format, ...) Trace(1, "%s:%d: " format "\n\r", __FILE__, __LINE__, ##__VA_ARGS__)

/**
 * @brief Macro for printing debug information with file and line info
 *
 * @param format Format string
 * @param ... Additional arguments
 */
#if IO_INTERFACE != 0 // !TRACE
#define uDebug(format, ...) \
  uPrintf(IO_INTERFACE, "%s:%d: " format "\n\r", __FILE__, __LINE__, ##__VA_ARGS__)
else
#define uDebug(format, ...) tDebug(format, ##__VA_ARGS__)
#endif

/**
 * @brief Macro for printing debug information based on UART I/O state
 * @param format Format string
 * @param ... Additional arguments
 */
#if DEBUG_LOG_ENABLE == 1
#if IO_INTERFACE != 0 // !TRACE
#define debug(format, ...) uDebug(format, ##__VA_ARGS__)
/**
 * @brief set print debug information to interface port selected
 */
#define setIOInterface() UART_Init(IO_INTERFACE, UART_IO_CONFIG);
#else
#define debug(format, ...) tDebug(format, ##__VA_ARGS__)
#define setIOInterface() ((void)0)
#endif // IO_INTERFACE
#else
#define debug(format, ...) ((void)0)
#endif

#define LIBS_DEBUG_I 15
#define LIBS_DEBUG_E 16

#endif