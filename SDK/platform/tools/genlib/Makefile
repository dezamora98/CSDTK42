# Name of the module
LOCAL_NAME := $(CURDIR)

# Depends module
LOCAL_MODULE_DEPENDS := ${SOFT_WORKDIR}/init\
						 ${SOFT_WORKDIR}/libs

# Set this to any non-null string to signal a module which
# generates a binary (must contain a "main" entry point). 
# If left null, only a library will be generated.
IS_ENTRY_POINT := no

# `yes` if have submodule or left empty  or `no`
IS_CONTAIN_SUB_MODULE := yes

# Assembly / C source code
S_SRC := 
C_SRC := 

include ${SOFT_WORKDIR}/platform/compilation/cust_rules.mk
