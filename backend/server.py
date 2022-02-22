from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.handlers import SimpleHandler

# curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http:localhost:8000


class fooHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("content-type", 'text/plain')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len).decode("utf-8")
        print(type(post_body))
        print(post_body)
        res = self.foo(post_body)
        self.wfile.write(res.encode())

    def foo(self, data):
        r = requests.get(url='http://google.com')
        return r


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), fooHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    print("runned")
    main()
