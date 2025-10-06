n=600851475143
i=2
last=1
while i*i<=n:
    if n%i==0:
        last=i
        n//=i
    else:
        i+=1 if i==2 else 2
if n>1:
    last=n
print(last)