import sys
import bluetooth

class bluetoothscreencontroller:
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    def __init__(self):
        self._bluetooth_conn = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    def connect_to_screen(self, bluetoothid, port=0x1001):
        self._bluetooth_conn.connect((bluetoothid, port))

    def disconnect_from_screen(self):
        self._bluetooth_conn.close()

    def send_command(self, command_line):
       self._bluetooth_conn.send("%s" % (command_line))

    def clear_screen(self):
       self._bluetooth_conn.send("clear")

    def draw_square_on_screen(self, color, pos=0, size=2):
       self._bluetooth_conn.send("square %s %s %s" %(color, pos, size))

    def draw_line_on_screen(self, color, dir="right", pos=0, size=2):
       self._bluetooth_conn.send("line %s %s %s %s" %(color, dir, pos, size))

"""
if sys.version < '3':
    input = raw_input

if len(sys.argv) < 2:
    print("usage: software.py <addr>")
    sys.exit(2)

sock = BluetoothScreenController(sys.argv[1])

#print("trying to connect to %s on PSM 0x%X" % (bt_addr, port))

sock.connect_to_screen()

print("connected.  type stuff")
while True:
    color = input()
    if(len(color) == 0): break
    amount = input()
    if(len(amount) == 0): amount = 1
    sock.send_command("%s %s" % (color, amount))
    data = sock._bluetooth_conn.recv(1024)
    print("Data received: %s %s" % (color , amount))

sock._bluetooth_conn.close()
"""
