import socket

PORT = 8000
HOST = ''
count = 0
print('HTTP server begins')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Launching HTTP server on " + str(HOST) + ":" + str(PORT))
print("Press Ctrl+C to exit.")

server.bind((HOST, PORT))
server.listen(5)

while True:
    clientSocket, address = server.accept()

    requestLine = clientSocket.recv(1024)
    
    requestLine = requestLine.split()
    requestDocument = requestLine[1].split('/')
    
    if (requestLine[0] == 'GET'):
        if (requestLine[1] == '/STATUS') | (requestLine[1] == '/status'):
            clientSocket.send("Server is running \n")
            clientSocket.send(str(count) + " documents has been succesfully served so far")
            print("Sent STATUS")
        elif requestLine[1][0] == '/':
            filename = requestDocument[1]
            try:
                openFile = open(filename, 'rb')
                count = count + 1
                content = openFile.read()
                clientSocket.send(content)
                openFile.close()
                print("Sent " + filename)
            except:
                clientSocket.send("404 Not Found \n")
                print("Could not find " + filename)
        else:
            clientSocket.send("400 Bad request \n")
            print("Bad request")
    else:
        clientSocket.send("400 Bad request \n")
        print("Bad request")
    clientSocket.close()
