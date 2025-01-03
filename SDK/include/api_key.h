#ifndef __API_KEY_H
#define __API_KEY_H
#include <api_event.h>

typedef enum{
    KEY_POWER = 0x4B,
    KEY_MAX
} Key_ID_t;

void Key_EventManagment_init(EventManagment_t fn);

#endif

