@echo off
adb shell media volume --show --stream 2 --set 0
adb shell media volume --show --stream 4 --set 1
adb shell media volume --show --stream 5 --set 0
