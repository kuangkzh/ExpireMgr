import threading
import time


class ExpireTimer:
    def __init__(self, expire_func, expire_time=30):
        self.create_time = time.time()
        self._expire_func = expire_func
        self._expire_time = expire_time
        self._timer = None
        self.modify_time = None
        self.access_time = None
        self.reset()

    def reset(self, expire_time=None):
        if expire_time:
            self._expire_time = expire_time
        if self._timer:
            self._timer.cancel()
            del self._timer
        self._timer = threading.Timer(self._expire_time, self._expire_func)
        self._timer.setDaemon(True)
        self.modify_time = time.time()
        self.access_time = self.modify_time
        self._timer.start()

    def refresh_access_time(self):
        self.access_time = time.time()

    def get_remain_time(self):
        return self.modify_time+self._expire_time-time.time()

    def __repr__(self):
        return str(self.get_remain_time())+"s"

    def __str__(self):
        return "ExpireTimer: remaining %f seconds" % self.get_remain_time()

    def __del__(self):
        if self._timer:
            self._timer.cancel()
            del self._timer
