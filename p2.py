num = [2,5,7,9,11,13,19,25,27,29,73,97,111]
for a in num:
    for i in range(2,int(a/2)):
        if a%i==0:
            print(a,"Not Prime")
            break
            
    else:
        print(a,"prime")
        




