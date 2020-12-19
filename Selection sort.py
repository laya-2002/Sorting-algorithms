                    # Selection Sort

# Defining a function used to sort the list elements using selection sort algorithm.
def selectionSort(li): 
    t=len(li)
    for i in range(t):
        min_ind=i 
        for j in range(i+1,t): 
            if(li[min_ind]>li[j]): 
                min_ind=j 
        (li[i],li[min_ind])=(li[min_ind],li[i]) 
    return li  

# Taking a list as input. 
s=list(map(int,input().split()))  

# Displaying the sorted list.
print(*selectionSort(s)) 
