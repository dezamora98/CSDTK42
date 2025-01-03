#include <api_event.h>
#include "api_os.h"

bool Event_free(API_Event_t *pevent)
{
    bool out = true;
    out = OS_Free(pevent->pParam1);
    out = OS_Free(pevent->pParam2);
    out = OS_Free(pevent);
    return out;
}