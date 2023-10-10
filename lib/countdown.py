# your code goes here!
import time

def countdown(num):
  while num > 0:
    print(f'{num} SECOND(S)!')
    num -= 1
print("Happy New Year")


def countdown_with_sleep(num):
  while num > 0:
    time.sleep(1)
    num -= 1
  print("Happy New Year")