import socket

header = 70
formaat = "utf-8"
server1 = socket.gethostbyname(socket.gethostname())
port = 5088
disconnect = "End"
addar = (server1,port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addar)

print("SERVER IS STARTING........")

server.listen()
print ("SERVER IS LISTENING ON", server1)


while True:
  conn,addr = server.accept()
  print("CONNECTED TO", addr)
  connect = True
  while connect:
    msg_l = conn.recv(header).decode(formaat)
    if msg_l:
      msg_length = int(msg_l)
      msg = conn.recv(msg_length).decode(formaat)
      if msg == disconnect:
        connect = False
        conn.send(f'Terminatting .... with {addr}'.encode(formaat))
      else:
        v = "aeiouAEIOU"
        c = 0

        for i in msg:
          if i in v:
            c+=1
          
        if c==0:
          conn.send("Not enough vowles".encode(formaat))
        elif c<=2:
          conn.send("Enough vowels I guess".encode(formaat))
        else:
          conn.send("Too many vowels".encode(formaat))
            
  conn.close()







