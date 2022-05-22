
from array import array
from asyncore import write
from fileinput import close
from heapq import heappop, heappush, heapify
import time
import random
import sys
#NAME:Sadik AKGEDIK                      NAME:Mustafa Tunahan BAS
#ID:150119052                            ID:150119055
#CSE2046 PROJECT1
#for the worst case of Quick-sort we needed to increase the recursion limit of python from 1000 to 2800. We couldn't increase more because of stack overflow problem.
sys.setrecursionlimit(2800)

#Creating heap from a random array using heapq library.
def createHeap(arr):
    heap=[]
    heapify(heap)
    #in order to build a max-heap we push the elements and multiply them with -1. otherwise it will be a min-heap
    for i in range(len(arr)):
        heappush(heap,-1*arr[i])
    
    return heap
#Quicksort function that calls Rec_quicksort in it with required lengths and so on   
def quickSort(arr):
    n=len(arr)
    return Rec_quicksort(arr, 0, n-1)
#This was for understanding and testing the Median of Three pivot selection,
def quicksortMedian(arr):
    n=len(arr)
    Rec_quicksortMedian(arr,0,n)

#Quicksort helper    
def Rec_quicksort(arr, first, last):
    if first<last:
        pos,i=partition(arr, first, last)
        Rec_quicksort(arr, first, pos-1)
        Rec_quicksort(arr, pos+1, last)
        return i
#Quicksort with median of three pivot selection helper.
def Rec_quicksortMedian(arr, first, last):
    if first<last:
        pos=partitionM3(arr, first, last)
        Rec_quicksortMedian(arr, first, pos)
        Rec_quicksortMedian(arr, pos+1, last)        
#Partitioning algorithm for quicksort 
def partition(arr, first, last):
    #We choose the first element as the pivot
    pivot=arr[first]
    i=first
    j=last
    #count is for counting the basic op.
    count=0
    while i<j:
        while i<=j and arr[i]<=pivot:
            i=i+1
            count+=1
        while pivot<arr[j]:
            j=j-1
            count+=1
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            count+=1
            
 
    temp=arr[first]
    arr[first]=arr[j]
    arr[j]=temp
    count+=1
    return j,count

#swap function used for partitioning with median of three pivot selection
def swap(array,a,b):
    array[a],array[b] = array[b],array[a]
#partitoning with median of three pivot selection
def partitionM3(array,start,end):
    count=0
    median = (end - 1 - start) // 2
    median = median + start
    
    left = start + 1
    #putting the last first and medium element in to correct places while picking the median of the three
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        swap(array,start,median)
        count+=1
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >=0:
        swap(array,start,end - 1)
        count+=1
    #median is at the first element now so we pick it as pivot
    pivot = array[start]
    for right in range(start,end):
        count+=1
        if pivot > array[right]:
            swap(array,left,right)
            left = left + 1
            count+=1
    swap(array,start,left-1)
    return left-1,count
#quick select algorithm
def quickSelect(arr, l, r, k):
    if (k >=0 and k <= r - l + 1):
 
        #Partition used in quicksort index is the position of partitioned element , o is for basic op
        index,o = partition(arr, l, r)
 
        #if position is the same as k
        if (index - l == k - 1):
            return arr[index]
 
        #If position is more, recur for left subarray
        if (index - l > k - 1):
            return quickSelect(arr, l, index - 1, k),o
        #Else recur for right subarray
        return quickSelect(arr, index + 1, r,
                            k - index + l - 1),o
    print("Index out of bound")
#Quick select with median of three partitoning
def quickSelectM3(arr,l,r,k):

    if (k > 0 and k <= r - l + 1):
        index,o = partitionM3(arr, l, r)
 
        #if position is the same as k
        if (index - l == k -1):
            return arr[index]
 
        #If position is more, recur for left subarray
        if (index - l > k-1 ):
            return quickSelectM3(arr, l, index - 1, k),o
 
        #Else recur for right subarray
        return quickSelectM3(arr, index + 1, r,
                            k - index + l - 1),o
    print("Index out of bound")

#Partia heap-sort algorithm. We pop the max element k times    
def partialheapSort(heap,k):
    count=0
    for i in range(len(heap)-k-1):
        heappop(heap)
        count=count+1
    return heap[0]*-1,count

#Merge sort Algorithm
def mergeSort(arr):
    count=0
    if len(arr) > 1:

        mid = len(arr)//2
       
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                count+=1
                
            else:
                arr[k] = R[j]
                j += 1
                count+=1
                
            k += 1
            count +=1
  
        # Checking if any element was left
        while i < len(L):
            count +=1
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            count+=1
            arr[k] = R[j]
            j += 1
            k += 1
    return count
#Insertion sort algorithm    
def insertionSort(arr):
    count=0 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                count=count+1
        arr[j + 1] = key
        #count=count+1
    return count
#Partial selection sort algorithm
def partialselectionSort(arr,size,k):
    count=0
    for i in range(k):
        minIndex=i
        minVal=arr[i]
        for j in range(i+1,size):
            if arr[j]<minVal:
                minIndex=j
                minVal=arr[j]
                arr[i],arr[minIndex]=arr[minIndex],arr[i]
                count=count+1
    return count


#These algorithms are for calculating the time complexities of algorithms used.

#Returns the time of merge-sort with given input
def calculatetimeofmerge(arr):
    start=time.process_time()
    count=mergeSort(arr)
    return time.process_time()-start,count

#Returns the time of Quick-sort with given input
def calculatetimeofquick(arr):
    start=time.process_time()
    count=quickSort(arr)
    return time.process_time()-start,count

#Returns the time of Partial Selection-sort with given input
def calculatetimeofPartialSelect(arr,size,k):
    start=time.process_time()
    count=partialselectionSort(arr,size,k)
    return time.process_time()-start,count

#Returns the time of insertion-sort with given input
def calculatetimeofinsert(arr):
    start=time.process_time()
    count=insertionSort(arr)
    return time.process_time()-start,count

#Returns the time of Quick Select algorithm with given input
def calculatetimeofQuickSelect(arr,size,k):
    start=time.process_time()
    i,count=quickSelect(arr,0,size-1,k)
    return time.process_time()-start,count

#Returns the time of Partial Heap-sort with given input
def calculatetimeofPartialHeap(heap,k):
    start=time.process_time()
    i,count=partialheapSort(heap,k)
    return time.process_time()-start

#Returns the time of Quick Select with median of three partitioning algorithm with given input
def calculatetimeofQuickSelectM3(arr,size,k):
    start=time.process_time()
    i,count=quickSelectM3(arr,0,size-1,k)
    return time.process_time()-start,count

#These algorithms are used for writing the times, list sizes , returned elements and basic op counts to txt files according to the algorithm.
#We used random library to create unsorted random lists of different sizes with given range.
def writemergetofile():
    file=open("mergesort.txt","w")
    start=100000
    size=150000
    while start<=size:
        arr=random.sample(range(0,int(start)),int(start))
        file.write(str(start)+"    "+str(calculatetimeofmerge(arr))+"\n")
        start=start+1000
    file=close()

def writepartialselectionsort():
    file=open("partialselectionsort.txt","w")
    start=1000
    size=5000
    while start<=size:
        arr=random.sample(range(0,int(start)),int(start))
        file.write(str(start)+"    "+str(int(start)/2)+"     "+str(calculatetimeofPartialSelect(arr,int(start),int(start/2)))+"\n")
        start=start+1000
    file=close()
#In partial selection sort and partial heap sort we divided the partial part in to percentiles while increasing list size simultaniously.
def writepartialselectionsortPercentile():
    file1=open("select10th.txt","w")
    file2=open("select20th.txt","w")
    file3=open("select30th.txt","w")
    file4=open("select40th.txt","w")
    file5=open("select50th.txt","w")
    file6=open("select60th.txt","w")
    file7=open("select70th.txt","w")
    file8=open("select80th.txt","w")
    file9=open("select90th.txt","w")
    file10=open("select100th.txt","w")
    size=10000
    
    
    while size <= 15000:
        k1=int(size*0.1)
        arr=random.sample(range(0,size),size)
        file1.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k1))+"\n")
        size = size+500
    file1=close()
    size=10000    
    while size <= 15000:
        k2=int(size*0.2)
        arr=random.sample(range(0,size),size)
        file2.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k2))+"\n")
        size = size+500
    file2=close()
    size=10000
    while size <= 15000:
        k3=int(size*0.3)
        arr=random.sample(range(0,size),size)
        file3.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k3))+"\n")
        size = size+500
    file3=close()
    size=10000
    while size <= 15000:
        k4=int(size*0.4)
        arr=random.sample(range(0,size),size)
        file4.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k4))+"\n")
        size = size+500
    file4=close()
    size=10000
    while size <= 15000:
        k5=int(size*0.5)
        arr=random.sample(range(0,size),size)
        file5.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k5))+"\n")
        size = size+500
    file5=close()
    size=10000
    while size <= 15000:
        k6=int(size*0.6)
        arr=random.sample(range(0,size),size)
        file6.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k6))+"\n")
        size = size+500
    file6=close()
    size=10000
    while size <= 15000:
        k7=int(size*0.7)
        arr=random.sample(range(0,size),size)
        file7.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k7))+"\n")
        size = size+500
    file7=close()
    size=10000
    while size <= 15000:
        k8=int(size*0.8)
        arr=random.sample(range(0,size),size)
        file8.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k8))+"\n")
        size = size+500
    file8=close()
    size=10000
    while size <= 15000:
        k9=int(size*0.9)
        arr=random.sample(range(0,size),size)
        file9.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k9))+"\n")
        size = size+500
    file9=close()
    size=10000
    while size <= 15000:
        k10=int(size)
        arr=random.sample(range(0,size),size)
        file10.write("size is:  "+str(size)+"  time and comp count is:  "+str(calculatetimeofPartialSelect(arr,size,k10))+"\n")
        size = size+500
    file10=close()

#It generates the list and sorts whether we want the best case or worst case.
def writequicktofile():
    val=input("Enter 1 for Best case  , 2 For Worst case: ")
    if val=="1":
        file1=open("quicksortBest.txt","w")
        start=100000
        size=150000
        while start<=size:
            arr=random.sample(range(0,int(start)),int(start))
            file1.write(str(start)+"    "+str(calculatetimeofquick(arr))+"\n")
            start=start+1000
    elif val=="2":
        file2=open("quicksortWorst.txt","w")
        start=1000
        size=2700
        while start<=size:
            arr=random.sample(range(0,int(start)),int(start))
            quickSort(arr)
            arr.reverse()
            file2.write(str(start)+"    "+str(calculatetimeofquick(arr))+"\n")
            start=start+10
        
    file1=close()
    file2=close()
                
def writeinserttofile():
    val=input("Enter 1 for Best case , 2 for Average , 3 For Worst case: ")
    if val == "1":
        file1=open("insertionBest.txt","w")
        start=10000
        size=100000
        while start<=size:
            arr=random.sample(range(0,int(start)),int(start))
            quickSort(arr)
            file1.write(str(start)+"    "+str(calculatetimeofinsert(arr))+"\n")
            start=start+500
    elif val == "2":
        start=1000
        size=10000
        file2=open("insertionAverage.txt","w")
        while start<=size:
            arr=random.sample(range(0,int(start)),int(start))
            file2.write(str(start)+"    "+str(calculatetimeofinsert(arr))+"\n")
            start=start+500
    elif val == "3":
        start=1000
        size=10000
        file3=open("insertionWorst.txt","w")
        while start<=size:
            arr=random.sample(range(0,int(start)),int(start))
            quickSort(arr)
            arr.reverse()
            file3.write(str(start)+"    "+str(calculatetimeofinsert(arr))+"\n")
            start=start+500
        
    file1=close() 
    file2=close()
    file3=close()            

def writequickSelecttofile(): 
    file=open("quickselect.txt","w")
 
    size =100000
    while size <= 150000:
        arr=random.sample(range(0,size),size)
        file.write(str(size)+"    "+str(calculatetimeofQuickSelect(arr,size,size//2))+"\n")
        size=size+1000
    file=close()              
        
def writepartialHeap():
    file=open("partialHeap.txt","w")
    start=100000
    size=110000
    while start<=size:
        arr=random.sample(range(0,int(start)),int(start))
        heap=createHeap(arr)
        file.write(str(start)+"    "+str(calculatetimeofPartialHeap(heap,len(heap)//2))+"     "+str(heap[0]*-1)+"\n")
        start=start+5000
    file=close()         

def writepartialHeapPercentile():
    file1=open("heap10th.txt","w")
    file2=open("heap20th.txt","w")
    file3=open("heap30th.txt","w")
    file4=open("heap40th.txt","w")
    file5=open("heap50th.txt","w")
    file6=open("heap60th.txt","w")
    file7=open("heap70th.txt","w")
    file8=open("heap80th.txt","w")
    file9=open("heap90th.txt","w")
    file10=open("heap100th.txt","w")
    
    
    size=100000
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k1=int(size*0.1)
        file1.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k1))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file1=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k2=int(size*0.2)
        file2.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k2))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file2=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k3=int(size*0.3)
        file3.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k3))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file3=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k4=int(size*0.4)
        file4.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k4))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file4=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k5=int(size*0.5)
        file5.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k5))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file5=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k6=int(size*0.6)
        file6.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k6))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file6=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k7=int(size*0.7)
        file7.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k7))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file7=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k8=int(size*0.8)
        file8.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k8))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file8=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k9=int(size*0.9)
        file9.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k9))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file9=close()
    while size<=150000:
        arr=random.sample(range(0,size),size)
        heap=createHeap(arr)
        k10=int(size)
        file10.write("size is :   "+str(size)+"  time is :  "+str(calculatetimeofPartialHeap(heap,k10))+"   "+str(heap[0]*-1)+"\n")
        size=size+500
    size=100000
    file10=close()

def writequickselectM3():
    file=open("quickselectM3.txt","w")
    size =100000
    
    while size <=150000:
        arr=random.sample(range(0,size),size)
        file.write(str(size)+"    "+str(calculatetimeofQuickSelectM3(arr,size,size//2))+"\n")
        size=size+1000
    file=close()


#A little menu for choosing the algorithm that we want tu run. It writes the output in to a txt file
val="1"
while val!="0":
    print("Enter input for choosing the algorithm please\n")
    print("\n")
    val=input("0 To exit \n1 for Insertion-sort\n2 for Merge-sort\n3 for Quick-sort\n4 for partial Selection-sort\n5 for partial Heap-sort\n6 for Quick-select\n7 for Quick-select with median of three\n")
    if val=="1":
        writeinserttofile()
    elif val=="2":
        writemergetofile()
    elif val=="3":
        writequicktofile()
    elif val=="4":
        writepartialselectionsortPercentile()
    elif val=="5":
        writepartialHeapPercentile()
    elif val=="6":
        writequickSelecttofile()
    elif val=="7":
        writequickselectM3()
        

    



