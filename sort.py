def bubbleSort(a,n):
    for num in range(n-1,0,-1):
        for i in range(num):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    print(a)
                
n=int(input("Enter the no. of numbers :"))
a = [int(x) for x in input().split()]
bubbleSort(a,n)
