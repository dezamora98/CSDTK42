#ifndef __API_SS_H_
#define __API_SS_H_

#include <sdk_init.h>
#include <api_event.h>


// uint32_t SS_SendUSSD(USSD_Type_t );
#define SS_SendUSSD    CSDK_FUNC(SS_SendUSSD)

void SS_EventManagment_init(EventManagment_t fn);

#endif
