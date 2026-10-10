n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  a=int(n)
  b=0
else:
  a=int(a)
  b=int(b)

p=[0,1,2,3,4,5,6,7]

if a not in p:
 k=int(a/8)
 l=str(int(a%8))
 while(k not in [1,2,3,4,5,6,7]):
  l=l+str(int(k%8))
  k=int(k/8)
 l=l+str(int(k))
 j=l[::-1]
else:
  j=str(p[a])

o=float("0."+str(b))
s=""
for _ in range(8):
  l=o*8
  k,d=str(float(l)).split(".")
  s=s+k
  o=float("0."+d)

  if o==0.0:
    break

print(j+"."+s)