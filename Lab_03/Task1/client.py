import socket

header = 70
formaat = "utf-8"
server = socket.gethostbyname(socket.gethostname())
port = 5088
disconnect = "End"
addar = (server,port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addar)

def send_msg(m):
  message = m.encode(formaat)
  msg_l = len(m)
  send_length = str(msg_l).encode(formaat)
  send_length += b" "*(header - len(str(msg_l)))


  client.send(send_length)
  client.send(message)

  print(client. recv (2048). decode (formaat))

msg = f"The hostname of client is {socket.gethostname()} and the IP is {server}"

send_msg(msg)
send_msg(disconnect)
