import socket

socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(('192.168.43.207',21))
    ans = s.recv(1024)
    print(ans.decode('utf-8'))
except Exception as e:
    print('[-] ERROR: '+str(e))
    