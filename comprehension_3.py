# dictionary comprehension using Python

rank = [1,2,3,4,5]
prog_lang = ["Python","Java","JavaScript","Go","C"]

print(rank)
print(prog_lang)

prog_rank ={key:value for (key,value)in zip(rank,prog_lang)}

print(prog_rank)

# another method 

dict1=([(i,i*2)for i in range(5)])
print(dict1)