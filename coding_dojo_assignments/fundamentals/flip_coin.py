import random

def flip_coin():
  return "heads" if random.random() < 0.5 else "tails"

def flip_n_coins(n):
  flips = {
    "heads": 0,
    "tails": 0
  }
  for _ in range(n):
    flips[flip_coin()] += 1
  return flips

print(flip_n_coins(5000))