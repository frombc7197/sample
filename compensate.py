HF = 528


for i in range(1,50):
    m = (int)(HF/i)
    e = HF - (m*i)
    c = (m*i)+e
    print(i,e,c,m)


print("----")

for i in range(1,50):
    m = HF%i
    e = HF-m
    print(i,m,e)

print("===")

for i in range(1,100):
    m = (int)(HF/i)
    e = HF - (m*i)
    k = HF%i    
    print(i,e,k)
    if(e != k):
        print("Unacceptable")
