
def findRelativeRanks(score):
    #sort score in descending order
    sc=sorted(score,reverse=True)
    count={}
    for i in range(len(sc)):
        if i==0:
            count[sc[i]]="Gold Medal"
        elif i==1:
            count[sc[i]]="Silver Medal"
        elif i==2:
            count[sc[i]]="Bronze Medal"
        else:
            count[sc[i]]=str(i+1)    
    result=[]
    for i in score:
     result.append(count[i])
    return result        
score=[10,3,8,9,4]
result=findRelativeRanks(score)
print(result)