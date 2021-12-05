#!/usr/bin/env python3

def perrin(num):
  if num == 0:
    return 3
  if num == 1:
    return 3
  if num == 2:
    return 2
  if num > 2:
    return perrin(num-2) + perrin(num-3)

print(perrin(50))
