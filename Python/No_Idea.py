# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
arr = list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))
#idhar a and b ko set mai krna imp hai
h=0
for i in arr:
    if i in a:
        h=h+1
    elif i in b:
        h=h-1
print(h)