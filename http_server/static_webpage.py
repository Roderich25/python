#http://localhost:8000/
import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Page not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Random title</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
