from http.server import BaseHTTPRequestHandler
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Kies willekeurig tussen statuscode 200 en 500
        status_code = random.choice([200, 500])
        
        # Stuur de gekozen statuscode
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Schrijf een bericht dat de status aangeeft
        message = f"Hello from Python! I'm sending you a {status_code} status."
        self.wfile.write(message.encode('utf-8'))
        return
