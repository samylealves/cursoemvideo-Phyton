from time import sleep
for c in range(10, -1,-1):
    sleep(1)
    print(c)
print('\33[1;31mBUM! BUM! POOWW\33[m!')