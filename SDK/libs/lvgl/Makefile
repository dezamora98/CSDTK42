# Name of the this module
LOCAL_NAME := $(CURDIR)


# Space-separated list of modules (libraries) your module depends upon.
# These should include the toplevel name, e.g. "libs/gps"
LOCAL_MODULE_DEPENDS := \


# Add includes from other modules we do not wish to link to
LOCAL_API_DEPENDS := ${SOFT_WORKDIR}/libs/utils \

# include folder
LOCAL_ADD_INCLUDE := ${SOFT_WORKDIR}/include \
                     ${SOFT_WORKDIR}/include/std_inc \
                     ${SOFT_WORKDIR}/include/api_inc \
                     ${LOCAL_NAME} \
                     ${LOCAL_NAME}/src \
                     ${LOCAL_NAME}/src/lv_core \
                     ${LOCAL_NAME}/src/lv_draw \
                     ${LOCAL_NAME}/src/lv_hal \
                     ${LOCAL_NAME}/src/lv_misc \
                     ${LOCAL_NAME}/src/lv_objx \
                     ${LOCAL_NAME}/src/lv_themes \

                    
# `yes` if have submodule or left empty  or `no`
IS_CONTAIN_SUB_MODULE := no

## ------------------------------------ ##
## 	Add your custom flags here          ##
## ------------------------------------ ##
MYCFLAGS += \

LOCAL_EXPORT_FLAG += LVGL_CONFIG_FILE=\"${CFG_LVGL_CONFIG_FILE}\"


## ------------------------------------- ##
##	List all your sources here           ##
## ------------------------------------- ##
S_SRC := ${notdir ${wildcard src/*.s}}
C_SRC := ${notdir ${wildcard ${LOCAL_NAME}/src/*.c}}
C_SRC_FILES +=  ${wildcard src/lv_core/*.c} \
                ${wildcard src/lv_draw/*.c} \
                ${wildcard src/lv_hal/*.c} \
                ${wildcard src/lv_misc/*.c} \
                ${wildcard src/lv_objx/*.c} \
                ${wildcard src/lv_themes/*.c} \
                ${wildcard src/lv_misc/lv_fonts/*.c} 



## ------------------------------------------------------------------- ##
##  Do Not touch below this line unless you know what you're doing.    ##
## ------------------------------------------------------------------- ##
include ${SOFT_WORKDIR}/platform/compilation/cust_rules.mk
