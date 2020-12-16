def insertionSort(li):
    t=len(li)
    for i in range(1,t,1):
        key=li[i] 
        j=i-1
        while(j>=0 and key<li[j]):
            li[j+1]=li[j] 
            j-=1 
        li[j+1]=key
    return li 
s=list(map(int,input().split())) 
print(*insertionSort(s))
