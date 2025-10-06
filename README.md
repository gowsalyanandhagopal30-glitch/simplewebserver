# EX01 Developing a Simple Webserver
## Date:05.10.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

```
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

```
## OUTPUT:

![alt text](<Screenshot (29).png>)


![alt text](<Screenshot (26).png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
