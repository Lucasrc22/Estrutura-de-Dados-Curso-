import socket

h = open('index.htm', 'r')
homepage = h.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
print(hex(id(s)))

s.bind(('', 8081))
s.listen(5)

try:
    while True:
        ws, addr = s.accept()
        print('newsock', ws)
        print('add', addr)
        data = ws.recv(2000)
        print("Requisição recebida:")
        print(data.split(b'\r\n')[0])
        
        P = data.split(b' ')  # GET / HTTP/1.0 -> [GET, /, HTTP/1.0]
        if P[0] == b'GET':
            if P[1] == b'/':
                resp = ('HTTP/1.1 200 OK\r\n'
                        'Content-Type: text/html\r\n'
                        'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' +
                        homepage)
                ws.sendall(resp.encode())
            else:
                filepath = P[1][1:].decode()  # transforma em string
                try:
                    with open(filepath, 'rb') as f:
                        figure = f.read()
                    ext = filepath.rpartition('.')[-1]  # pega extensão (jpg, png, gif...)
                    response = ('HTTP/1.1 200 OK\r\n'
                                f'Content-Type: image/{ext}\r\n'
                                f'Content-Length: {len(figure)}\r\n\r\n')
                    ws.sendall(response.encode())
                    ws.sendall(figure)
                except FileNotFoundError:
                    resp = "HTTP/1.1 404 Not Found\r\n\r\nArquivo não encontrado"
                    ws.sendall(resp.encode())

except KeyboardInterrupt:
    print(" terminado pelo usuario")

ws.close()
s.close()
