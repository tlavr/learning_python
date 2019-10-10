import sys, os
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

curdir = os.getcwd()
home = curdir +"\home"

if not os.path.exists(home): os.mkdir(home, 0o777)

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        my_file = str(self.path).split("/")[1]
        content = self.get_content(my_file)
        self.send_response(200) #200 - stranica naidena
        self.send_header("content-type","text/html; charset=utf-8")
        self.wfile.write(content.encode())
        
    def get_content(self, my_file):
        try:
            file_path = home + "\\" + my_file
            print("fp==", file_path)
            file = open(r"" + file_path, "r", encoding = "utf-8")
        except(OSError, Exception) as e:
            print(e)
        else:
            content = file.read()
        return content
    
        
serv = HTTPServer(("localhost", 9040),HttpProcessor)

serv.serve_forever()


