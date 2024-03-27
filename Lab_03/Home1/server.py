import socket

header = 70
formaat = "utf-8"
server1 = socket.gethostbyname(socket.gethostname())
port = 5088
disconnect = "End"
addar = (server1, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addar)

print("SERVER IS STARTING........")

server.listen()
print("SERVER IS LISTENING ON", server1)


def calculate_salary(hours_worked):
    if hours_worked <= 40:
        salary = hours_worked * 200
    else:
        salary = 8000 + (hours_worked - 40) * 300
    return salary


while True:
    conn, addr = server.accept()
    print("CONNECTED TO", addr)
    connect = True
    while connect:
        msg_l = conn.recv(header).decode(formaat)
        if msg_l:
            msg_length = int(msg_l)
            msg = conn.recv(msg_length).decode(formaat)
            if msg == disconnect:
                connect = False
                conn.send(f'Terminating .... with {addr}'.encode(formaat))
            else:
                try:
                    hours_worked = int(msg)
                    salary = calculate_salary(hours_worked)
                    conn.send(f"Salary: Tk {salary}".encode(formaat))
                except ValueError:
                    conn.send("Invalid input. Please enter a valid number of hours.".encode(formaat))

    conn.close()
