# ==================================== #
#        control-tuya_smarthome        #
#                Lampki                # 
# ==================================== #

# ------------ import libs ----------- #
import tinytuya
import constants # file

# --------------- magic -------------- #

device = tinytuya.OutletDevice(constants.Lampki_device_ID, constants.Lampki_device_IP, constants.Lampki_device_key) # device = Lampki

device.set_version(3.3) # Tuya protocol version

data = device.status() # get info about device (on/off, mode, etc.)
# print(data) # debug
# print(data.get('dps',{}).get('1')) # debug

if data.get('dps',{}).get('1') == True: # check device's status to see if it's turned on or off
    print('Device is turned ON.')
    print('Switching OFF...')
    device.turn_off()
else:
    print('Device is turned OFF.')
    print('Switching ON...')
    device.turn_on()
print('Done.')