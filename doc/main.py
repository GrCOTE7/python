
#templates = gabarits (fr)
from string import Template

t = Template("${village}folk send $$10 to $cause.")

g = t.substitute(village="Nottingham", cause="the ditch fund")
print(g)

t = Template("Return the $item to $owner.")
d = dict(item="unladen swallow")
# t.substitute(d) → Error

print(t.safe_substitute(d))
