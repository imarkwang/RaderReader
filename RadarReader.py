import serial
# a = '8004000400016e1a'
# a_bytes = bytes.fromhex(a)
# print(a_bytes)
# aa = a_bytes.hex()
# print(aa)

ser = serial.Serial("COM3", 9600, timeout=0.5)
# print(ser.name)

# print(ser.port)
ser.close()
# print(ser.isOpen())
ser.open()
# print(ser.isOpen())
# check_sensor = '\x80\x04\x00\x04\x00\x01\x6e\x1a'.encode('iso-8859-15')
# get_flow_rate = '\x80\x04\x00\x01\x00\x01\x7e\x1b'.encode('iso-8859-15')
# get_flow_rate_direct = '\x80\x04\x00\x02\x00\x01\x8e\x1b'.encode('iso-8859-15')
# get_hor_angle = '\x80\x04\x00\x06\x00\x01\xcf\xda'.encode('iso-8859-15')
# get_ver_angle = '\x80\x04\x00\x07\x00\x01\x9e\x1a'.encode('iso-8859-15')

get_flow_rate = bytes.fromhex('8004000100017e1b')
get_flow_rate_direct =  bytes.fromhex('8004000200018e1b')
get_hor_angle = bytes.fromhex('800400060001cfda')
get_ver_angle =  bytes.fromhex('8004000700019e1a')
ser.write(get_flow_rate)
flow_rate_b = ser.read(10)
# print(flow_rate_b)
# print(flow_rate_b.hex())
# print(flow_rate_b[1])
# print(type(flow_rate_b[1]))

flow_rate = flow_rate_b[4]/100

print("flow rate: %0.4f"%flow_rate)

ser.write(get_flow_rate_direct)
flow_rate_direct_b = ser.read(10)
# print(flow_rate_direct_b)
# print(flow_rate_direct_b.hex())
flow_rate_direct = flow_rate_direct_b[4]
print("flow rate direction: %d"%flow_rate_direct)

ser.write(get_hor_angle)
hor_angle_b = ser.read(10)
# print(hor_angle_b)
# print(hor_angle_b.hex())
hor_angle = (hor_angle_b[3]*256+hor_angle_b[4])/100
# print(hor_angle)
print("horizontal angle: %0.4f"%hor_angle)


ser.write(get_ver_angle)
ver_angle_b = ser.read(10)
# print(ver_angle_b)
# print(ver_angle_b.hex())
ver_angle = (ver_angle_b[3]*256+ver_angle_b[4])/100
# print(ver_angle)
print("vertical angle: %0.4f"%ver_angle)
# ser.write('\x80\x04\x00\x05\x00\x01\x3f\xda'.encode('iso-8859-15'))

ser.close()

