#Returner alle primtall lavere enn N

primtall = []
for i in range(2, 21):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primtall.append(i)
        

            

print(primtall)
