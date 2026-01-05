import numpy as np
import random as r
def game():
  leg_moved=0
  arr=np.array(["up","down","right","left"])
  #leg_initial=np.random.choice(list(arr),2)
  leg_initial=r.sample(list(arr),2)
  print(leg_initial)
  N=int(input("enter the output:"))
  for i in range(N):
    choices=r.choice(arr)
    print(choices)
    if choices in leg_initial:
      continue
    else:
      leg_initial[0]=choices
      leg_moved+=1
  print(leg_moved)
if __name__ == "__main__":
  game()