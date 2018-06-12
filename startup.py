import webview
import threading
from server import run_server


def url_ok(url, port):
    # Use httplib on Python 2
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception("Server not started")
        return False

if __name__ == "__main__":

    t = threading.Thread(target=run_server)
    t.daemon = True
    t.start()

    while not url_ok("192.168.4.1", 24):
        sleep(0.1)

    webview.create_window("","http://192.168.4.1/",fullscreen=False)
