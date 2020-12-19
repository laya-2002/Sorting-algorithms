                   # Bubble Sort

# Function used to sort a list using Bubble sort algorithm. 
def bubbleSort(li):
    t=len(li)
    for i in range(t-1):
        for j in range(0,t-i-1,1):
            if(li[j]>li[j+1]):
                (li[j],li[j+1])=(li[j+1],li[j])
    return li 

# Taking list as input. 
s=list(map(int,input().split()))  

# Displaying the sorted list. 
print(*bubbleSort(s))
