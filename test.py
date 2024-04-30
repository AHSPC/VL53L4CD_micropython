from machine import I2C, Pin
from vl53l4cd import VL53L4CD

# Make sure to set the correct pins!
i2c = I2C(id=0, sda=Pin(0), scl=Pin(1))

vl53 = VL53L4CD(i2c)

# OPTIONAL: can set non-default values
vl53.inter_measurement = 0
vl53.timing_budget = 20

print("VL53L4CD Simple Test.")
print("--------------------")
model_id, module_type = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Timing Budget: {}".format(vl53.timing_budget))
print("Inter-Measurement: {}".format(vl53.inter_measurement))
print("--------------------")

vl53.start_ranging()

while True:
    ### OLD
    # while not vl53.data_ready:
    #     pass
    # vl53.clear_interrupt()
    # print("Distance: {} cm".format(vl53.distance))

    ### NEW (convenience method):
    dist = vl53.get_distance()
    print(f"Distance: {dist} cm")
