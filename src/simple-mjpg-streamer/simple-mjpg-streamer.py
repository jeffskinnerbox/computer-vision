#!/usr/bin/python3
'''
    Author: Igor Maculan - n3wtron@gmail.com
    A Simple mjpg stream http server - https://gist.github.com/n3wtron/4624820
    Jeff Irland ported to Python3
'''
import cv2
#import Image
from PIL import Image
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler,HTTPServer
#from SocketServer import ThreadingMixIn
from socketserver import ThreadingMixIn
#import StringIO
import io
import time


capture = None


class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header(b'Content-type',
                             b'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
                try:
                    rc, img = capture.read()
                    if not rc:
                        continue
                    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    jpg = Image.fromarray(imgRGB)
#                    tmpFile = StringIO.StringIO()
#                    tmpFile = io.StringIO()
                    tmpFile = io.BytesIO()
                    jpg.save(tmpFile, 'JPEG')
                    self.wfile.write(b"--jpgboundary")
                    self.send_header(b'Content-type', b'image/jpeg')
 #                   self.send_header(b'Content-length', str(tmpFile.len))
                    self.send_header(b'Content-length', tmpFile.getbuffer().nbytes)
                    self.end_headers()
                    jpg.save(self.wfile, 'JPEG')
                    time.sleep(0.05)
                except KeyboardInterrupt:
                    break
            return
        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header(b'Content-type', b'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head></head><body>')
 #           self.wfile.write(b'<img src="http://127.0.0.1:8080/cam.mjpg"/>')
            self.wfile.write(b'<img src="http://127.0.0.1:8080/home/jeff/src/zetta-demo/tools/jsmpeg/view-stream.html"/>')
            self.wfile.write(b'</body></html>')
            return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def main():
    global capture
#    capture = cv2.VideoCapture(0)
    capture = cv2.VideoCapture("/home/jeff/Jupyter-Notebooks/videos/People-Walking-Shot-From-Above.mp4")
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    capture.set(cv2.CAP_PROP_SATURATION, 0.2)
    global img

    try:
        server = ThreadedHTTPServer(('localhost', 8080), CamHandler)
        print("server started")
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()

if __name__ == '__main__':
    main()
