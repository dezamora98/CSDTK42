## ----------------------------------------------------------- ##
## Don't touch the next line unless you know what you're doing.##
## ----------------------------------------------------------- ##

LOCAL_NAME := $(CURDIR)

# List of submodules which contain code we need to include in the final lib
LOCAL_MODULE_DEPENDS :=  ${SOFT_WORKDIR}/init\
                         ${SOFT_WORKDIR}/libs/utils

LOCAL_API_DEPENDS := \


# include folder
LOCAL_ADD_INCLUDE := ${SOFT_WORKDIR}/include \
                     ${SOFT_WORKDIR}/include/std_inc \
                     ${SOFT_WORKDIR}/include/api_inc \
                     $(LOCAL_NAME)/include\
                    
# Set this to any non-null string to signal a module which 
# generates a binary (must contain a "main" entry point). 
# If left null, only a library will be generated.
IS_ENTRY_POINT := yes

## ------------------------------------ ##
## 	Add your custom flags here          ##
## ------------------------------------ ##
MYCFLAGS += 

## ------------------------------------- ##
##	List all your sources here           ##
## ------------------------------------- ##
C_SRC := ${notdir ${wildcard ${LOCAL_NAME}/src/*.c}}

## ------------------------------------- ##
##  Do Not touch below this line         ##
## ------------------------------------- ##
include ${SOFT_WORKDIR}/platform/compilation/cust_rules.mk