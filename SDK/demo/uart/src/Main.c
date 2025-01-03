#include <stdbool.h>
#include <stdio.h>
#include <api_os.h>
#include <api_hal_uart.h>
#include <stdlib.h>

void Main(void *pData)
{
    UART_Init(UART1, (UART_Config_t){
                         .baudRate = UART_BAUD_RATE_115200,
                         .dataBits = UART_DATA_BITS_8,
                         .errorCallback = NULL,
                         .parity = UART_PARITY_NONE,
                         .rxCallback = NULL,
                         .stopBits = UART_STOP_BITS_1,
                         .useEvent = false});

    char msg[] = "hello word\n\r";

    while (true)
    {
        UART_Write(0, (uint8_t *)msg, strlen(msg));
        OS_Sleep(500);
    }
}
