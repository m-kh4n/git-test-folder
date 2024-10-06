import http.server
import socketserver

# Define the port you want to run your server on
PORT = 8080

# Define a request handler that will serve the HTML content
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code to 200 (OK)
        self.send_response(200)
        
        # Set the headers (Content-type for HTML)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Write the HTML response
        self.wfile.write(b"<html><head><title>Hello</title></head><body><h1>Hello, World!</h1></body></html>")

# Create a TCPServer instance
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Run the server, until interrupted
    httpd.serve_forever()
