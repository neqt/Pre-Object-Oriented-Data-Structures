def countdown(n):
    if(listt[n-1]==listt[n]-1):
        list1.append(listt[n])
        return countdown(n-1)
    elif(listt[n]==1):
       # list1.clear()
        return n
    elif(listt[n-1]!=listt[n]-1):
        return -1
list1=[]
list2=[]
print("*** Fun with countdown ***")
print("Enter List : ", end = '')
listt = [int(n) for n in input().split()]
for i in range(len(listt)):
    if(countdown(i)!=-1):
        list2.append(list1)
        i=countdown(i)
   # elif(countdown(i)==-1):
        #list1.clear()
print(list2)