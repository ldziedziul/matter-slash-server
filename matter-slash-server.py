#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# coding=utf-8
import json
import logging
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler

from handlers import EuroCommandHandler
from mattermostrequest import MattermostRequest

HOSTNAME = 'localhost'
PORT = 8088

log = logging.getLogger(__name__)

class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        post_data = self.read_post_data()

        log.info("received " + str(post_data))
        request = MattermostRequest(post_data)
        responsetext = None

        if request.command[0] == u'/euro':
            responsetext = EuroCommandHandler().handle(request)

        if responsetext:
            data = {}
            # 'response_type' may also be 'in_channel'
            data['response_type'] = 'ephemeral'
            data['text'] = responsetext
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data))
        return

    def read_post_data(self):
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        return post_data

def setup_logging():
    logging.basicConfig(format='%(asctime)s [%(module)s] %(message)s')
    log.setLevel(logging.INFO)

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    setup_logging()
    server = HTTPServer((HOSTNAME, PORT), PostHandler)
    log.info("Starting matterslash server http://%s:%s" % (HOSTNAME, PORT))
    log.info("Press Ctrl+C or send SIGINT to exit")
    server.serve_forever()
