import time

tt = 0  # all
t = 0
i = 1  # variables conditions

while i > 0:
    time.sleep(120)
    t += 1
    tt += 1
    if t == 9:
        t = t - t
    else:
        continue
