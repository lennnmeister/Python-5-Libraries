import random

"""

#below, w/o "from", we import everything in the module "random"
import random

#square brackets [ ] indicate its a list. 
#parentheses belong to choice function
#it specify where its parameters get passed in.

coin = random.choice(["heads", "tails"])
print(coin)

##using this specific. we skip "random." 

from random import choice

coin = choice(["heads", "tails"])
print(coin)

#calling the library random. it has a funtion called randint = random integer
#it takes 2 args: betweeen a & b, both a & b inclusive

number = random.randint(1,10)
print(number)

"""


## randon.shuffle(x) allows you to shuffle

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
for carddd in cards:
  print(carddd)