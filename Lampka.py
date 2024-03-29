# ==================================== #
#        control-tuya_smarthome        #
#                Lampka                #
# ==================================== #

# ------------ import libs ----------- #
import tinytuya
import constants # file 

# --------------- magic -------------- #

device = tinytuya.BulbDevice(constants.Lampka_device_ID, constants.Lampka_device_IP, constants.Lampka_device_key) # device = Lampka

device.set_version(3.3) # Tuya protocol version

data = device.status() # get info about device (on/off, mode, etc.)
# print(data) # debug
# print(data.get('dps',{}).get('20')) # debug

if data.get('dps',{}).get('20') == True: # check device's status to see if it's turned on or off
    print('Device is turned ON.')
    print('Switching OFF...')
    device.turn_off()
else:
    print('Device is turned OFF.')
    print('Switching ON...')
    device.turn_on()
print('Done.')