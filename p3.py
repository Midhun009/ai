dataarr=[]
with open('3.csv') as f:
    for line in f:
        dataarr.append(line.strip().split(','))

rows=len(dataarr)
cols=len(dataarr[0])
shypo=['0']*(cols-1)
ghypo=[['?']*(cols-1)]
print("Initial Specific Hypothesis:",shypo)
print("Initial General Hypothesis:",ghypo)

for x in range(1,rows):
    lst=dataarr[x]

    if lst[cols-1]=='1':
        for i in range(0,cols-1):
            if shypo[i]==lst[i]:
                continue
            shypo[i]='?' if shypo[i]!='0' else lst[i]
            for g in ghypo:
                if g[i]!='?' and shypo[i]=='?':
                    ghypo.remove(g)   
    
    elif lst[cols-1]=='0':
        ghypo.clear()
        for i in range(0,cols-1):
            if lst[i]!=shypo[i] and shypo[i]!='?':
                temp_list=['?']*i + [shypo[i]] + (['?']*(cols-2-i))
            if temp_list not in ghypo:
                ghypo.append(temp_list)

    print("Specific hypothesis after row ",x," is: ",shypo)
    print("General hypothesis after row ",x," is: ",ghypo)

print("Final Specific Hypothesis: ",shypo)
print("Final General Hypothesis: ",ghypo)