#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <api_os.h>
#include <api_event.h>
#include <api_debug.h>
#include <api_key.h>
#include <api_inc_pm.h>
#include <api_ss.h>
#include <api_sms.h>
#include <api_hal_uart.h>
#include <api_gps.h>
#include <api_call.h>
#include <api_network.h>
#include <api_socket.h>
#include <api_fota.h>
#include <sdk_default.h>
#include <sdk_init.h>
/*#########################################################################################*/
/*please don't change anything in the following function*/

void user_Init(T_INTERFACE_VTBL_TAG *pVtable);
T_INTERFACE_VTBL_TAG *g_InterfaceVtbl = 0;
typedef struct T_VTBL_TAG
{
    const uint32_t magic;
    void (*user_init)(T_INTERFACE_VTBL_TAG *pVtable);
} T_VTBL_TAG;
static const volatile T_VTBL_TAG __attribute__((__section__(".section_init")))
g_s_UserVtbl =
    {
        (uint32_t)0x87654321,
        user_Init,
        // user_main,
}; //

extern char __user_rw_lma;
extern char __user_rw_start;
extern char __user_rw_size;
extern char __user_bss_start;
extern char __user_bss_size;

volatile uint32_t *temp000___;

extern void Main(void *pData);
static void StartUserAPP(void *);
static void OSTask(void *pv);
static bool bootState = true;

static HANDLE mainTaskHandle = NULL;
static HANDLE osTaskHandle = NULL;
static bool SysReady = false;

static EventManagment_t EventManagment_KEY = NULL;
static EventManagment_t EventManagment_PM = NULL;
static EventManagment_t EventManagment_USSD = NULL;
static EventManagment_t EventManagment_SMS = NULL;
static EventManagment_t EventManagment_UART = NULL;
static EventManagment_t EventManagment_GPS = NULL;
static EventManagment_t EventManagment_CALL = NULL;
static EventManagment_t EventManagment_NETWORK = NULL;
static EventManagment_t EventManagment_SOCKET = NULL;

void Key_EventManagment_init(EventManagment_t fn)
{
    EventManagment_KEY = fn;
}
void PM_EventManagment_init(EventManagment_t fn)
{
    EventManagment_PM = fn;
}
void SS_EventManagment_init(EventManagment_t fn)
{
    EventManagment_USSD = fn;
}
void SMS_EventManagment_init(EventManagment_t fn)
{
    EventManagment_SMS = fn;
}
void UART_EventManagment_init(EventManagment_t fn)
{
    EventManagment_UART = fn;
}
void GPS_EventManagment_init(EventManagment_t fn)
{
    EventManagment_GPS = fn;
}
void NETWORK_EventManagment_init(EventManagment_t fn)
{
    EventManagment_NETWORK = fn;
}

bool getSysReady(void)
{
    return SysReady;
}

HANDLE getOsTaskHandle(void)
{
    return osTaskHandle;
}

HANDLE getMainTaskHandle(void)
{
    return mainTaskHandle;
}

void StartUserAPP(void *vp)
{
    debug("User APP START");
    mainTaskHandle = OS_CreateTask(Main, NULL, NULL, USER_APP_STACK_SIZE, MAX_TASK_PR, 0, 0, "MainTask");
    OS_StopCallbackTimer(osTaskHandle, StartUserAPP, NULL);
    bootState = false;
}

/*#########################################################################################*/
void user_Main(void)
{
    temp000___ = (uint32_t *)&g_s_UserVtbl.magic;
    osTaskHandle = OS_CreateTask(OSTask, NULL, NULL, 2048, MAX_TASK_PR - 1, 0, 0, "OSTask");
    OS_SetUserMainHandle(&osTaskHandle);
}
void user_Init(T_INTERFACE_VTBL_TAG *pVtable)
{
    memset(&__user_bss_start, 0, (uint32_t)&__user_bss_size);
    memcpy(&__user_rw_start, &__user_rw_lma, (uint32_t)&__user_rw_size);
    g_InterfaceVtbl = pVtable;
    user_Main();
}
/*#########################################################################################*/

#if ENABLE_UART_FOTA != 0
#define FOTA_UART_HEADER "fsize"
#define FOTA_UART_SIZE sizeof(FOTA_UART_HEADER) - 1

#define FOTA_UartInit(uart, config) UART_Init(uart, config)

static void FOTA_ReceivedFileData(uint8_t *data, uint16_t len)
{
    static int fotasize = 0;
    uint32_t pos = (uint32_t)strstr(data, "\r\n");
    debug("uart received data,length:%d,data: %d, pos: ", len, (pos));
    MEMBLOCK_Trace(1, data, len, 16);
    if (fotasize == 0 && memcmp(data, FOTA_UART_HEADER, FOTA_UART_SIZE) == 0)
    {
        fotasize = atoi(data + FOTA_UART_SIZE);
        debug("uart fotasize:%d len:%d", fotasize, len);
        if (fotasize)
        {
            if (!API_FotaInit(fotasize))
                goto F_upgrade_faile;
            else
                OS_StopCallbackTimer(osTaskHandle, StartUserAPP, NULL);
        }
    }
    else if (fotasize)
    {
        debug("uart fota,fotasize:%d len:%d", fotasize, len);
        if (API_FotaReceiveData(data, len) == 0)
            goto F_upgrade_faile;
    }

F_upgrade_faile:
    debug("uart fota false");
    API_FotaClean();
    return;
}

/*
static void FOTA_ReceivedData(uint8_t *data, uint16_t len)
{
    static int fotasize = 0;
    debug("uart received data,length:%d,data:%s %d", len, data, FOTA_UART_SIZE);
    MEMBLOCK_Trace(1, data, len, 16);
    if (fotasize == 0 && memcmp(data, FOTA_UART_HEADER, FOTA_UART_SIZE) == 0)
    {
        fotasize = atoi(data + FOTA_UART_SIZE);
        debug("uart fotasize:%d len:%d", fotasize, len);
        if (fotasize)
        {
            if (!API_FotaInit(fotasize))
                goto upgrade_faile;
            else
                OS_StopCallbackTimer(osTaskHandle, StartUserAPP, NULL);
        }
    }
    else if (fotasize)
    {
        debug("uart fota,fotasize:%d len:%d", fotasize, len);
        if (API_FotaReceiveData(data, len) == 0)
            goto upgrade_faile;
    }
    return;

upgrade_faile:
    debug("uart fota false");
    // API_FotaClean();
    return;
}
*/
#endif // !ENABLE_UART_FOTA


static void OSTask(void *pv)
{
    API_Event_t *pEvent = NULL;
    setIOInterface();


#if ENABLE_UART_FOTA != 0
    FOTA_UartInit(UART1, DEFAULT_FOTA_UART_CONFIG);
#endif

    OS_StartCallbackTimer(osTaskHandle, USER_APP_START_MS, StartUserAPP, NULL);

    while (true)
    {
        if (OS_WaitEvent(osTaskHandle, (void **)&pEvent, OS_TIME_OUT_WAIT_FOREVER))
        {
            switch (pEvent->id)
            {
            // power
            case API_EVENT_ID_POWER_INFO: // param1: (PM_Charger_State_t<<16|charge_level(%)) , param2: (PM_Battery_State_t<<16|battery_voltage(mV))
            case API_EVENT_ID_POWER_ON:   // param1: shows power on cause:
                if (EventManagment_PM != NULL)
                    EventManagment_PM(pEvent);
                break;

            // System
            case API_EVENT_ID_SYSTEM_READY:
                SysReady = true;
                break;

            // ERROR
            case API_EVENT_ID_MALLOC_FAILED:
                Assert(false, "MALLOC_FAILED");
                break;

            // keypad
            case API_EVENT_ID_KEY_DOWN: // param1:key id(Key_ID_t)
            case API_EVENT_ID_KEY_UP:   // param1:key id(Key_ID_t)
                if (EventManagment_KEY != NULL)
                    EventManagment_KEY(pEvent);
                break;

            // ussd
            case API_EVENT_ID_USSD_IND:          // pParam1: USSD_Type_t
            case API_EVENT_ID_USSD_SEND_SUCCESS: // pParam1: USSD_Type_t
            case API_EVENT_ID_USSD_SEND_FAIL:    // param1:error code(USSD_Error_t) param2:error code2(USSD_Error_t)
                if (EventManagment_USSD != NULL)
                    EventManagment_USSD(pEvent);
                break;

            // SMS
            case API_EVENT_ID_SMS_SENT:
            case API_EVENT_ID_SMS_RECEIVED:     // param1:SMS_Encode_Type_t, param2:message content length, pParam1:message header info, pParam2:message content
            case API_EVENT_ID_SMS_ERROR:        // param1:SMS_Error_t cause
            case API_EVENT_ID_SMS_LIST_MESSAGE: // pParam1:SMS_Message_Info_t*(!!!pParam1->data need to free!!!)
                if (EventManagment_SMS != NULL)
                    EventManagment_SMS(pEvent);
                break;

            // UART
            case API_EVENT_ID_UART_RECEIVED: // param1: uart number, param2: length, pParam1: data
                if (EventManagment_UART != NULL)
                    EventManagment_UART(pEvent);

#if ENABLE_UART_FOTA != 0
                else if (bootState)
                {
                    uint8_t data[pEvent->param2 + 1];
                    data[pEvent->param2] = 0;
                    memcpy(data, pEvent->pParam1, pEvent->param2);
                    FOTA_ReceivedFileData(data, pEvent->param2);
                }
#endif // ENABLE_UART_FOTA
                break;

            // GPS
            case API_EVENT_ID_GPS_UART_RECEIVED: // param1: length, pParam1: data
                if (EventManagment_GPS != NULL)
                    EventManagment_GPS(pEvent);
                break;

            // CALL
            case API_EVENT_ID_CALL_DIAL:     // param1: isSuccess, param2:error code(CALL_Error_t)
            case API_EVENT_ID_CALL_HANGUP:   // param1: is remote release call, param2:error code(CALL_Error_t)
            case API_EVENT_ID_CALL_INCOMING: // param1: number type, pParam1:number
            case API_EVENT_ID_CALL_ANSWER:
            case API_EVENT_ID_CALL_DTMF: // param1: key
                if (EventManagment_CALL != NULL)
                    EventManagment_CALL(pEvent);
                break;

            // Network
            case API_EVENT_ID_NETWORK_REGISTERED_HOME:
            case API_EVENT_ID_NETWORK_REGISTERED_ROAMING:
            case API_EVENT_ID_NETWORK_REGISTER_SEARCHING:
            case API_EVENT_ID_NETWORK_REGISTER_DENIED:
            case API_EVENT_ID_NETWORK_REGISTER_NO:
            case API_EVENT_ID_NETWORK_DEREGISTER:
            case API_EVENT_ID_NETWORK_DETACHED:
            case API_EVENT_ID_NETWORK_ATTACH_FAILED:
            case API_EVENT_ID_NETWORK_ATTACHED:
            case API_EVENT_ID_NETWORK_DEACTIVED:
            case API_EVENT_ID_NETWORK_ACTIVATE_FAILED:
            case API_EVENT_ID_NETWORK_ACTIVATED:
            case API_EVENT_ID_NETWORK_GOT_TIME:  // pParam1: RTC_Time_t*
            case API_EVENT_ID_NETWORK_CELL_INFO: // param1:cell number(1 serving cell and param1-1 neighbor cell) , pParam1: Network_Location_t*
                if (EventManagment_NETWORK != NULL)
                    EventManagment_NETWORK(pEvent);
                break;

            // Socket\DNS
            case API_EVENT_ID_SOCKET_CONNECTED: // param1: socketFd
            case API_EVENT_ID_SOCKET_CLOSED:    // param1: socketFd
            case API_EVENT_ID_SOCKET_SENT:      // param1: socketFd
            case API_EVENT_ID_SOCKET_RECEIVED:  // param1: socketFd, param2: length of data received
            case API_EVENT_ID_SOCKET_ERROR:     // param1: socketFd, param2: error cause(API_Socket_Error_t)
            case API_EVENT_ID_DNS_SUCCESS:      // param1:IP address(uint32_t), pPram1:domain(char*), pParam2:ip(char*)
            case API_EVENT_ID_DNS_ERROR:
                if (EventManagment_SOCKET != NULL)
                    EventManagment_SOCKET(pEvent);
                break;

            default:
                break;
            }

            Event_free(pEvent);
        }
    }
}