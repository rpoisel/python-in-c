from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler


def mul(a, b):
    print("Will compute", a, "times", b)
    c = 0
    for i in range(0, a):
        c = c + b
    return c


def factory():
    s = Sample()
    return s.calc()


class Sample(object):

    def __init__(self):
        pass

    def calc(self):
        return 42


class MyHandler(SimpleHTTPRequestHandler):

    def __init__(self, req, client_addr, server):
        SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)


    def do_GET(self):
        response = "<h1>Hello World</h1>"
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))
        self.wfile.flush()


def httpd():
    port = 8000
    print("serving at port", port)
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()


