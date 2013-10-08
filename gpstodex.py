def gpstodex(d,m,s):
    result = d+(m*(1/60))+(s*(1/3600))
    return result

print(gpstodex(131,52,10))
print(gpstodex(124,10,47))
print(gpstodex(33,6,37))
print(gpstodex(43,00,36))

print(gpstodex(37,58,87))
print(gpstodex(126,40,63))
