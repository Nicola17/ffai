import pytest
import ffai.web.server as server
import requests
from multiprocessing import Process, Queue
import time


def test_server():
    def start():
        server.start_server(debug=True, use_reloader=False, port=3405)
    p = Process(target=start)
    p.start()
    time.sleep(1)
    url = "http://localhost:3405/"
    r = requests.get(url=url, params={})
    assert r.status_code == 200
    p.kill()


if __name__ == "__main__":
    test_server()