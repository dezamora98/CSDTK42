
#ifndef _ASSERT_H_
#define _ASSERT_H_

#include "sdk_init.h"

#define __assert CSDK_FUNC(__assert)

void Assert(bool valid, const char *fmt);

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)
#define ASSERT_MSG "File: " __FILE__ " | Line: " TOSTRING(__LINE__)
#define assert(valid) Assert(valid, ASSERT_MSG)

#endif
