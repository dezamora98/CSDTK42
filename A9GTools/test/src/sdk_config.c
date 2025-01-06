#include <sdk_config.h>

SDK_Config_t sdk_config = {
    .io_interface = TRACE,
    .enable_fota = false,
    .enable_log_dispach = false,
    .user_app_start_delay_ms = 5000,
    .user_app_StackSize = 2048
};
