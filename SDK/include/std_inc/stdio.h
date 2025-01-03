#ifndef STDIO_H
#define STDIO_H

#ifdef __cplusplus
extern "C"
{
#endif

#include "stddef.h"
#include <stdarg.h>
#include "sdk_init.h"
#include "sdk_config.h"
#include "api_debug.h"
#include "api_hal_uart.h"

#ifndef EOF
#define EOF (-1)
#endif

/**
 * @brief Custom sprintf function
 *
 * This macro replaces the standard sprintf function.
 * It calls the SDK-provided implementation.
 *
 * @param buf Buffer to store the formatted string
 * @param fmt Format string
 * @param ... Additional arguments
 * @return int Number of characters written
 */
#define sprintf CSDK_FUNC(sprintf)

/**
 * @brief Custom snprintf function
 *
 * This macro replaces the standard snprintf function.
 * It calls the SDK-provided implementation.
 *
 * @param buf Buffer to store the formatted string
 * @param len Maximum number of characters to write
 * @param fmt Format string
 * @param ... Additional arguments
 * @return int Number of characters written
 */
#define snprintf CSDK_FUNC(snprintf)

/**
 * @brief Custom sscanf function
 *
 * This macro replaces the standard sscanf function.
 * It calls the SDK-provided implementation.
 *
 * @param buf Buffer to read the formatted input
 * @param fmt Format string
 * @param ... Additional arguments
 * @return int Number of input items successfully matched and assigned
 */
#define sscanf CSDK_FUNC(sscanf)

/**
 * @brief Custom vsprintf function
 *
 * This macro replaces the standard vsprintf function.
 * It calls the SDK-provided implementation.
 *
 * @param buf Buffer to store the formatted string
 * @param fmt Format string
 * @param ap List of arguments
 * @return int Number of characters written
 */
#define vsprintf CSDK_FUNC(vsprintf)

/**
 * @brief Custom vsnprintf function
 *
 * This macro replaces the standard vsnprintf function.
 * It calls the SDK-provided implementation.
 *
 * @param buf Buffer to store the formatted string
 * @param size Maximum number of characters to write
 * @param fmt Format string
 * @param ap List of arguments
 * @return int Number of characters written
 */
#define vsnprintf CSDK_FUNC(vsnprintf)

/**
 * @brief Custom vsscanf function
 *
 * This macro replaces the standard vsscanf function.
 * It calls the SDK-provided implementation.
 *
 * @param fp String to read the formatted input
 * @param fmt0 Format string
 * @param ap List of arguments
 * @return int Number of input items successfully matched and assigned
 */
#define vsscanf CSDK_FUNC(vsscanf)

/**
 * @brief Custom printf function
 *
 * This macro replaces the standard printf function.
 * It checks the UART I/O state and directs the output
 * to either uPrintf or tPrintf.
 *
 * @param format Format string
 * @param ... Additional arguments
 */
#define printf(format, ...)                   \
    {                                         \
        if (sdkConfig.io_interface != TRACE) \
            uPrintf(format, ##__VA_ARGS__);   \
        else                                  \
            tPrintf(format, ##__VA_ARGS__);   \
    }

#ifdef __cplusplus
}
#endif

#endif /* STDIO_H */
