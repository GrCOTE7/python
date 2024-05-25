from timeit import Timer

total_time = 0
for i in range(200):
    t = Timer("t=a; a=b; b=t", "a=1; b=2")
    total_time += t.timeit()
print(f"Temps total : {round(total_time,2)} secondes")

total_time = 0
for i in range(200):
    t = Timer("a,b = b,a", "a=1; b=2")
    total_time += t.timeit()
print(f"Temps total : {round(total_time,2)} secondes")


