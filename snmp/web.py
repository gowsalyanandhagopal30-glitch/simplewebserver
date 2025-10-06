from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
<head>
<title>device description</title>
</head>
<body>
<h2 align="center">Device specification-(N.Gowsalya)</h2>
<table border="3">
<tr bgcolor="lightgreen">
<th>S.NO</th>
<th>Device specification</th>
<th>Type</th>
</tr>
<tr>
<td>1</td>
<td>DeviceName</td>
<td>LAPTOP-J2KOGH51</td>
</tr>
<tr>
<td>2</td>
<td>Processor</td>
<td>13th Gen Intel(R) Core(TM)i5-1334U</td>
</tr>
<tr>
<td>3</td>
<td>InstalledRAM</td>
<td>16.0GB</td>
</tr>
<tr>
<td>4</td>
<td>Device ID</td>
<td>3804009E-57E2-4B25-1E26152390D4</td>
</tr>
<tr>
<td>5</td>
<td>System type</td>
<td>64-bit operating system</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()