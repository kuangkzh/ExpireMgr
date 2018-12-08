import uuid
import hashlib
from ExpireDict import ExpireDict


class ExpireToken:
    def __init__(self, expire_time=300, access_refresh=True):
        self._token_dick = ExpireDict(expire_time, access_refresh)

    def new_token(self):
        token = hashlib.sha1(uuid.uuid1().bytes).hexdigest()
        self._token_dick[token] = {}
        return token

    def __call__(self):
        return self.new_token()

    def get_session(self, token):
        try:
            return self._token_dick[token]
        except KeyError:
            return None
    __getitem__ = get_session

    def del_session(self, token):
        try:
            del self._token_dick[token]
        except KeyError:
            return
    __delitem__ = del_session

    def get_create_time(self, token):
        return self._token_dick.get_create_time(token)

    def get_remain_time(self, token):
        return self._token_dick.get_remain_time(token)

    def __str__(self):
        return self._token_dick.__str__()
    __repr__ = __str__
