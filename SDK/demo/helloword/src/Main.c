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
