n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  a=n
  b=""
  w=int(a)
  d=0
else:
  w=int(a)
  d=int(b[::-1])
k=w
c=0
sum1=0
for _ in range(len(a)):
  l=int(k%10)
  sum1=sum1+(l*(2**c))
  c=c+1
  k=int(k/10)

k=d
c=1
sum2=0
for _ in range(len(b)):
  l=int(k%10)
  sum2=sum2+(l/(2**c))
  c=c+1
  k=int(k/10)

print(sum1+sum2)

  
