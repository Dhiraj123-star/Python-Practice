# random.seed() determines a random number generator's outcome
# therefore,if it stays the same, the outcome will continue to be the
# same.

import random
random.seed(2)
a=[12,45,100]
random.shuffle(a)
print(a)
random.seed(2)
random.shuffle(a)
print(a)