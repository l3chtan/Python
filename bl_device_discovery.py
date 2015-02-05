import bluetooth

target_name = "Rigani"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
	if target_name == bluetooth.lookup_name( bdaddr ):
		target_address = bdaddr
		break

if target_address is not None:
	print ("Found: "  + target_name)
else:
	print ("No device found")

