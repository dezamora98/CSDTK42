#include <api_os.h>
#include <stdbool.h>
#include <stdio.h>
#include <api_hal_gpio.h>

void Main(void *pData)
{
    GPIO_config_t led = {
        .mode         = GPIO_MODE_OUTPUT,
        .pin          = GPIO_PIN27,
        .defaultLevel = GPIO_LEVEL_LOW,
    };

    GPIO_Init(led);

    while (true)
    {
        printf("Hello, Word!\n\r");
        OS_Sleep(500);
        GPIO_SetLevel(led, GPIO_LEVEL_HIGH);
        printf("Hello, Word!\n\r");
        OS_Sleep(500);
        GPIO_SetLevel(led, GPIO_LEVEL_LOW);
    }
}
