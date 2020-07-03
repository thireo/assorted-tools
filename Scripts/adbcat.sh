pid=$(adb shell ps -o NAME -o PID | grep danishcare | cut -f2 -d' ')
#echo $pid
adb logcat --pid $pid -v color
