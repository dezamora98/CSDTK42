# Name of the this module
LOCAL_NAME := $(CURDIR)


# Space-separated list of modules (libraries) your module depends upon.
# These should include the toplevel name, e.g. "libs/gps"
LOCAL_MODULE_DEPENDS := ${SOFT_WORKDIR}/libs/utils \
                        ${SOFT_WORKDIR}/libs/gps \
                        ${SOFT_WORKDIR}/libs/cjson \
                        ${SOFT_WORKDIR}/libs/tiny-json \
                        
ifeq "$(strip ${CFG_LCD_SUPPORT})" "y"
    LOCAL_MODULE_DEPENDS += ${SOFT_WORKDIR}/libs/lcd 
endif

ifeq "$(strip ${CFG_LVGL_SUPPORT})" "y"
    LOCAL_MODULE_DEPENDS += ${SOFT_WORKDIR}/libs/lvgl 
endif

# Add includes from other modules we do not wish to link to
LOCAL_API_DEPENDS := \


# include folder
LOCAL_ADD_INCLUDE := \


                    
# `yes` if have submodule, or left empty  or `no`
IS_CONTAIN_SUB_MODULE := yes

## ------------------------------------ ##
## 	Add your custom flags here          ##
## ------------------------------------ ##
MYCFLAGS += \

## ------------------------------------- ##
##	List all your sources here           ##
## ------------------------------------- ##
S_SRC := ${notdir ${wildcard src/*.s}}
C_SRC := ${notdir ${wildcard ${LOCAL_NAME}/src/*.c}}


## ------------------------------------------------------------------- ##
##  Do Not touch below this line unless you know what you're doing.    ##
## ------------------------------------------------------------------- ##
include ${SOFT_WORKDIR}/platform/compilation/cust_rules.mk
