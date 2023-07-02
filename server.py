from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/my_page.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200) #OK
        except:
            file_to_open = "File not found"
            self.send_response(404) #not found
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8')) #to write in web page

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
