from ExpireToken import ExpireToken
from ExpireDict import ExpireDict
import time

ept = ExpireToken(1, True)
t1 = ept()
t2 = ept()
print(ept)
time.sleep(0.5)
ept[t1]["x"] = 1
print(ept)
time.sleep(0.5)
print(ept)
