pid=$(adb shell ps | grep danishcare | cut -f8-9 -d' ')
adb logcat --pid $pid -v color