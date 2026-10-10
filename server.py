import http.server
from proxy import CachingProxy

def run_server(original, port):
    proxy_instance = CachingProxy(original, port)

    class ProxyRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            response = proxy_instance.handel_request(self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response)

    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, ProxyRequestHandler) 
    print(f"Starting proxy server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down proxy server.")
        httpd.server_close()