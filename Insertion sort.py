# Function used to sort a list using Insertion sort algorithm. 
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

# Taking a list as input.
s=list(map(int,input().split())) 

# Displaying the sorted list.
print(*insertionSort(s))
