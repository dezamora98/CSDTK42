#include <stdbool.h>
#include <stdio.h>
#include <api_os.h>
#include <api_hal_gpio.h>

void Main(void *pData)
{
    GPIO_Init((GPIO_config_t){.mode = GPIO_MODE_OUTPUT,
                              .pin = GPIO_PIN27,
                              .defaultLevel = GPIO_LEVEL_LOW});

    while (true)
    {
        GPIO_Set(GPIO_PIN27, GPIO_LEVEL_HIGH);
        printf("LED ON");
        OS_Sleep(1000);
        GPIO_Set(GPIO_PIN27, GPIO_LEVEL_LOW);
        printf("LED OFF");
        OS_Sleep(1000);
    }
}
