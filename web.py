from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 1em;
            text-align: left;
        }
        th, td {
            padding: 12px 15px;
            border: 1px solid #ddd;
        }
        thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }
        tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }
        tbody tr:hover {
            background-color: #f1f1f1;
        }
        tbody tr.layer-header {
            font-weight: bold;
            background-color: #d1d1d1;
            color: #333;
        }
    </style>
</head>
<body>

    <h1>TCP/IP Protocol Suite</h1>
    <p>This table outlines the four layers of the TCP/IP model, along with their primary functions and examples of the protocols that operate at each layer.</p>

    <table>
        <thead>
            <tr>
                <th>Layer</th>
                <th>Function</th>
                <th>Examples of Protocols</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="layer-header" colspan="3">Application Layer</td>
            </tr>
            <tr>
                <td></td>
                <td>Provides high-level protocols for direct interaction with user applications, such as file transfers and email.</td>
                <td>
                    <ul>
                        <li><b>HTTP:</b> HyperText Transfer Protocol</li>
                        <li><b>FTP:</b> File Transfer Protocol</li>
                        <li><b>SMTP:</b> Simple Mail Transfer Protocol</li>
                        <li><b>DNS:</b> Domain Name System</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td class="layer-header" colspan="3">Transport Layer</td>
            </tr>
            <tr>
                <td></td>
                <td>Responsible for end-to-end communication, managing data flow, and ensuring data is delivered correctly.</td>
                <td>
                    <ul>
                        <li><b>TCP:</b> Transmission Control Protocol (reliable, connection-oriented)</li>
                        <li><b>UDP:</b> User Datagram Protocol (unreliable, connectionless)</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td class="layer-header" colspan="3">Internet Layer</td>
            </tr>
            <tr>
                <td></td>
                <td>Handles addressing and routing of data packets across different networks to their final destination.</td>
                <td>
                    <ul>
                        <li><b>IP:</b> Internet Protocol (IPv4, IPv6)</li>
                        <li><b>ICMP:</b> Internet Control Message Protocol</li>
                        <li><b>ARP:</b> Address Resolution Protocol</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td class="layer-header" colspan="3">Network Access Layer</td>
            </tr>
            <tr>
                <td></td>
                <td>Defines how data is transmitted physically over the network hardware, including framing and error detection.</td>
                <td>
                    <ul>
                        <li><b>Ethernet:</b> Defines how data is transmitted over a wired LAN</li>
                        <li><b>Wi-Fi (802.11):</b> Standard for wireless local area networking</li>
                        <li><b>PPP:</b> Point-to-Point Protocol</li>
                    </ul>
                </td>
            </tr>
        </tbody>
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