from cv2 import __version__
import uuid
import json
import ts_dweepy        # https://pypi.python.org/pypi/dweepy/
import time


class TraceMess:

    def __init__(self, src):
        self.run_stamp = {
            "mess-type": "EXEC",
            "mess-format": "0.0.2",
            "run-id": str(uuid.uuid4()),
            "run-time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "run-status": "start",
            "run-platform": "Desktop-Jupyter",
            "run-source": src,
            "version": {
                "algorithm": "0.0.3",
                "cv2": __version__
            }
        }
        print(json.dumps(self.run_stamp))

    def start(self):
        self.run_stamp["run-status"] = "start"
        self.run_stamp["run-time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())    #noqa
        print(json.dumps(self.run_stamp))

    def stop(self):
        self.run_stamp["run-status"] = "stop"
        self.run_stamp["run-time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())    #noqa
        print(json.dumps(self.run_stamp))

    def error(self, mess):
        print(json.dumps({"mess-type": "ERROR","run-id": self.run_stamp["run-id"], "mess-text": mess}))       #noqa

    def warning(self, mess):
        print(json.dumps({"mess-type": "WARNING","run-id": self.run_stamp["run-id"], "mess-text": mess}))     #noqa

    def info(self, mess):
        print(json.dumps({"mess-type": "INFO","run-id": self.run_stamp["run-id"], "mess-text": mess}))        #noqa

    def feature(self, mess):
        ts_dweepy.dweet_for(self.run_stamp["run-platform"], {"mess-type": "FEATURE","run-id": self.run_stamp["run-id"], "mess-text": mess})     #noqa
        print(json.dumps({"mess-type": "FEATURE","run-id": self.run_stamp["run-id"], "mess-text": mess}))     #noqa
