from random import choice

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$?"

ln = 14
cnt = 5

for _ in range(cnt):
    print("".join([choice(CHARS) for _ in range(ln)]))
