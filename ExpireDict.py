from ExpireTimer import ExpireTimer


class ExpireDict(dict):
    def __init__(self, expire_time=30, access_refresh=True, modify_refresh=True):
        super().__init__()
        self._timers = {}
        self.expire_time = expire_time
        self.access_refresh = access_refresh
        self.modify_refresh = modify_refresh

    def __getitem__(self, item):
        if self.access_refresh:
            self._timers[item].reset()
        else:
            self._timers[item].refresh_access_time()
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if not self._timers.__contains__(key):
            self._timers[key] = ExpireTimer(lambda: self.__delitem__(key), self.expire_time)
        elif self.access_refresh or self.modify_refresh:
            self._timers[key].reset()
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        try:
            del self._timers[key]
            return super().__delitem__(key)
        except KeyError:
            return

    def get_create_time(self, key):
        return self._timers[key].create_time

    def get_modify_time(self, key):
        return self._timers[key].modify_time

    def get_access_time(self, key):
        return self._timers[key].access_time

    def get_remain_time(self, key):
        return self._timers[key].get_remain_time()

    def __repr__(self):
        return "Data:"+super().__repr__()+"\nExpire time:"+self._timers.__repr__()
    __str__ = __repr__
