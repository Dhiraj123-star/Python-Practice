# generate even numbers through generator comprehension 
import random
generate_even = (num for num in range(random.randint(1,100)) if num%2==0)

for i in generate_even:
    print(i)