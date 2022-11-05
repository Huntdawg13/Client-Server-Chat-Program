import socket

IP = socket.gethostbyname(socket.gethostname())
Address = (IP, 5000)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect(Address)
    
    message = input("Enter here --> ")
    
    while message.lower().strip() != 'leaving chat':  
        if message.__contains__(".txt" or ".docx" or ".pdf" or ".py"):
            file = open(message)
            data = file.read()
            client.send(message.encode())
            msg = client.recv(1024).decode()
            print(msg)
            client.send(data.encode())
            msg = client.recv(1024).decode()
            print(msg)
            file.close()
            
            message = input("Enter here --> ")
        else:
            client.send(message.encode())
            data = client.recv(1024).decode()

            print('Received from server: ' + data)

            message = input("Enter here --> ")
            
    client.close()
    
if __name__ == "__main__":
    main()