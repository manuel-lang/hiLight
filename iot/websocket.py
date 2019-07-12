import websockets


cam = [0,0,1]
sens = 88
user = 50

def make_socket_string(message):
    strings = []
    if type(message) == int:
        for i in range(6):
            hex_value= hex(message).upper()[2:]
            strings.append('{"datalen":1,"srcraw":0,"src":"local","datahex":"%s","sender":"se","type":"groupwrite","time":1562939923,"dstraw":2310,"dst":"1\/1\/%d"}'%(hex_value, i+1))
    else:
        for idx, pos_value in enumerate(message):
            hex_value = "FF" if pos_value>2 else "00"
            strings.append('{"datalen":1,"srcraw":0,"src":"local","datahex":"%s","sender":"se","type":"groupwrite","time":1562939923,"dstraw":2310,"dst":"1\/1\/%d"}'%(hex_value, (2*idx)+1))
            strings.append('{"datalen":1,"srcraw":0,"src":"local","datahex":"%s","sender":"se","type":"groupwrite","time":1562939923,"dstraw":2310,"dst":"1\/1\/%d"}'%(hex_value, (2*idx)+2))

    return strings
        
print("-"*30)
make_socket_string(cam)
print("-"*30)
make_socket_string(sens)
print("-"*30)
make_socket_string(user)
