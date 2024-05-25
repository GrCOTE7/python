from timeit import Timer

nfois = 300

# v1
total_time = 0
for i in range(nfois):
    t = Timer("t=a; a=b; b=t", "a=1; b=2")
    total_time += t.timeit()
print(f"Temps total v1 ({nfois} iter.): {round(total_time,2)} secondes")

# v2
total_time = 0
for i in range(nfois):
    t = Timer("a,b = b,a", "a=1; b=2")
    total_time += t.timeit()
print(f"Temps total v2 ({nfois} iter.): {round(total_time,2)} secondes")
