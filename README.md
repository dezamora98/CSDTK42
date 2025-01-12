# A9G_SDK Project

This repository contains an enhanced SDK for the AiThinker A9G development board. The main feature is the inclusion of `A9GTools`, a command-line interface tool that simplifies project creation and management. Currently, `A9GTools` is only available for Windows.

[![Video demonstration](https://img.youtube.com/vi/G1WOhVJ2Qkk/0.jpg)](https://www.youtube.com/watch?v=G1WOhVJ2Qkk)

## A9GTools

A9GTools provides the following commands to streamline your workflow:

* **-install**: Add A9Gtools to the environment variables so that it can be used from any path in the project **(it is necessary to run this command for the first time before starting to use A9GTools)**.

** **update**: Update A9Gtools through the https://github.com/dezamora98/CSDTK42

* **create**: Create a new A9G_SDK project.

* **build**: Build the project.

* **fota**: Build the project and create a FOTA package (requires a previous compilation of the project in the hex folder).

* **clean**: Delete project builds.

* **coolwatcher**: Open CoolWatcher.
____

## Project Structure and Requirements

To ensure that your project works correctly with the modified SDK and the A9GTools command-line interface, it is essential to follow the folder structure defined by the A9GTools create command. This structure is designed to organize your project files and dependencies in a way that facilitates compilation and development.

When you create a new project using the **A9GTools create <project_name>** command, the following folder structure is generated:

```/
<project_name>/
├── include/
│   └── sdk_config.h
├── src/
│   └── Main.c
└── Makefile
```

**1. Makefile:**

* Description: The Makefile contains the build instructions for your project. It defines how the source files should be compiled and linked, and it is essential for automating the build process.

**2. src:**

Description: The src directory must contain all the sources of the project (.c) where one of them contains the **void Main(void*)** function, which is essential to start your project.

**Simple example of file <project_name>/src/Main.c:**

```C
#include <api_os.h>
#include <stdbool.h>
#include <stdio.h>

void Main(void *pData)
{
    while (true)
    {
        printf("Hello, Word!\n\r");
        OS_Sleep(500);
    }
}
```

**2. include:**

* Description: the **include** directory must contain all project headers or other header directories, and must also contain the sdk_config.h file. This configuration file includes various settings needed for the SDK. It must be located in the **include** directory and must be configured correctly to match the requirements of your project.

**Simple example of file <project_name>/include/sdk_config.h:**

```C
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
```

____

## SDK Configuration Guide

This guide explains how to configure the SDK for the A9G development board using the mandatory `sdk_config.h` file located in the `include` directory.

### I/O Interface Selection (IO_INTERFACE)

0. TRACE: Use the trace interface for I/O
1. UART1: Use UART1 interface for I/O
2. UART2: Use UART2 interface for I/O

### UART I/O Configuration (UART_IO_CONFIG)

Initializes a *UART_Config_t* structure with specific settings for UART I/O, including baud rate, data bits, error callback, parity, stop bits, and event usage.

### Firmware Over-the-Air (FOTA) Enable Settings (ENABLE_UART_FOTA)

0. Disabled: FOTA is not enabled
1. UART1: FOTA through UART1
2. UART2: FOTA through UART2

### Default UART Configuration for FOTA (DEFAULT_FOTA_UART_CONFIG)

Initializes a UART_Config_t structure with default settings for FOTA, including baud rate, data bits, stop bits, parity, receive callback, and event usage.

### Debug Logging Enable Settings (DEBUG_LOG_ENABLE)

0. Disabled: Debug logging is not enabled
1. Enabled: Debug logging is enabled

### User Application Start Delay (USER_APP_START_MS)

Defines the delay time in milliseconds before the user application starts.

### User Application Stack Size (USER_APP_STACK_SIZE)

Defines the stack size allocated for the user application in bytes.

How to Use
Include the sdk_config.h File: Ensure that the sdk_config.h file is located in the include directory of your project.

Modify Configuration Options: Edit the sdk_config.h file to set the desired configuration options for your project.

Build Your Project: Use A9GTools to create, build, and manage your project with the configured settings.

____

## Implementation of *printf* and *debug* Functions

In this SDK implementation, the behavior of the printf function is defined by the configuration in the file **<project_name>/include/sdk_config.h**, according to the value of the **IO_INTERFACE** macro. The output of printf can be directed to one of the UART interfaces or to the **Trace function from the original SDK**, which outputs to the **MMI 01** channel of the **Trace plugin** in the **CoolWatcher tool**.

The **printf** and **debug** functions in this SDK uses the configuration defined by the IO_INTERFACE macro to determine where to send its output:

**The IO_INTERFACE macro specifies the interface for output:**

```C
// I/O Interface selection:
// 0 - TRACE: Use the trace interface for I/O
// 1 - UART1: Use UART1 interface for I/O
// 2 - UART2: Use UART2 interface for I/O
#define IO_INTERFACE 0
```

To enable or disable the debug function, set the DEBUG_LOG_ENABLE macro in sdk_config.h:

```c
// Debug logging enable settings:
// 0 - Disabled: Debug logging is not enabled
// 1 - Enabled: Debug logging is enabled
#define DEBUG_LOG_ENABLE 1
```

The debug feature is an alternative debugging tool that is especially useful since the debug options do not yet work on the development board. It provides context by including the file path, aiding in the identification and resolution of problems.

____

## Event Management in the New SDK

In this implementation of the new SDK, there is no need to create an event dispatcher. We have implemented a callback system to handle all the peripheral events from the SoC, which were previously managed by the default SDK. This new system simplifies the event management process and makes the code more modular and easier to maintain.

The developer is responsible for handling the events triggered by the peripheral within each callback, considering that some peripherals can generate different events even though they share the same callback according to the enumeration of events defined in [api_event.h](SDK\include\api_inc\api_event.h) of the original SDK:

```C
void Key_EventManagment_init(EventManagment_t fn);
void PM_EventManagment_init(EventManagment_t fn);
void SS_EventManagment_init(EventManagment_t fn);
void SMS_EventManagment_init(EventManagment_t fn);
void UART_EventManagment_init(EventManagment_t fn);
void UART_EventManagment_init(EventManagment_t fn);
void GPS_EventManagment_init(EventManagment_t fn);
void NETWORK_EventManagment_init(EventManagment_t fn);
```

By using these initialization functions, developers can easily set up custom callback functions for different events, ensuring that the appropriate actions are taken for each event type.

## [More information about the features of the original SDK](SDK\README.md)

## [Local SDK_API information summary](SDK\doc\SUMMARY.md)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or support, please contact [Daniel E. Zamora](dezamora98@gmail.com).
