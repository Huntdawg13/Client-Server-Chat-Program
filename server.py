from distutils.log import info
import socket


IP = socket.gethostbyname(socket.gethostname())
theAddress = (IP, 5000)

def main():
    print("Starting up")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(theAddress)
    server.listen(5)
    conn, theaddress = server.accept()
    print(f"Connected: {theaddress}.")
    
    while True:        
        info = conn.recv(1024).decode()
        if info.__contains__(".txt" or ".docx" or ".pdf" or ".py"):
            print(f"Receiving file.")
            file = open(info, "w")
            conn.send("File received.".encode())
            data = conn.recv(1024).decode()
            print(f"Receiving data.")
            file.write(data)
            conn.send("Data received".encode())
            file.close()
        else:
            print("Anonymous: " + str(info))
            info = input('Enter here --> ')
            conn.send(info.encode())        
    conn.close()
        
if __name__ == "__main__":
    main()