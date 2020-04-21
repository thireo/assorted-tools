import subprocess

file = open("output.txt",'w+')

addr = ""
checksum = 0
calcedChecksum = 0
sensorErrors = []
boxErrors = []
states = []

returnVal = subprocess.run(['nrfjprog', '--memrd', '512000', '--w','8','--n','256'],capture_output=True)
#print('-----------------------------')
#print(returnVal.stdout.decode('utf-8').split(' '))
#print('-----------------------------')
addr = returnVal.stdout.decode('utf-8').split(' ')[2:8]
print('BLE ADDR:\t',addr)
file.write('BLE ADDR:\t%s\n'%addr)
checksum = int(returnVal.stdout.decode('utf-8').split(' ')[8],16)
print('Checksum:\t',hex(checksum))
file.write('Checksum:\t%s\n'%hex(checksum))
for byte in addr:
    calcedChecksum += int(byte,16)
calcedChecksum = calcedChecksum % 256


print('Calc. Checksum:\t',hex(calcedChecksum))
file.write('Calc. Checksum:\t%s\n'%hex(calcedChecksum))
temp = []
for error in returnVal.stdout.decode('utf-8').split(' ')[20:20+16:2]:
    temp.append(int(error,16))
    #print(int(error,16))
boxErrors.append(temp)
temp = []
for error in returnVal.stdout.decode('utf-8').split(' ')[21:21+16:2]:
    temp.append(int(error,16))
boxErrors.append(temp)
print('Box Errors:\t',boxErrors)
file.write('Box Errors:\t%s\n'%boxErrors)

temp = []
for error in returnVal.stdout.decode('utf-8').split(' ')[39:39+16:2]:
    temp.append(int(error,16))
    #print(int(error,16))
sensorErrors.append(temp)
temp = []
for error in returnVal.stdout.decode('utf-8').split(' ')[40:40+16:2]:
    temp.append(int(error,16))
sensorErrors.append(temp)
print('Sensor Errors:\t',sensorErrors)
file.write('Sensor Errors:\t%s\n'%sensorErrors)
#returnVal = subprocess.run(['nrfjprog', '--memrd', '512118', '--w','8','--n','128'],capture_output=True)

#states.append(int(returnVal.stdout.decode('utf-8').split(' ')[3],16))
offset2States = 136
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+6:offset2States+14])
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+17:offset2States+33])
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+36:offset2States+52])
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+55:offset2States+71])
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+74:offset2States+90])
states.extend(returnVal.stdout.decode('utf-8').split(' ')[offset2States+93:offset2States+95])
ss = []
for state in states:
    #print(state)
    ss.append(int(state,16))
states = ss

print('States:\t\t',states)
file.write('States:\t\t%s\n'%states)

returnVal = subprocess.run(['nrfjprog', '-d'],capture_output=True)
print(returnVal.stdout.decode('utf-8'))
file.close()