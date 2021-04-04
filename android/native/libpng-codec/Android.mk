LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_SYSTEM_SHARED_LIBRARIES := libc libpng liblog
LOCAL_LDLIBS := -lpng -llog -g
LOCAL_MODULE_PATH := $(TARGET_OUT_OPTIONAL_EXECUTABLES)
LOCAL_SRC_FILES := main.cpp
LOCAL_MODULE := png-codec
LOCAL_CFLAGS += -Wno-error

LOCAL_C_INCLUDES += \
    external/libpng/ \
    system/core/include \
    system/core/libsync

include $(BUILD_EXECUTABLE)