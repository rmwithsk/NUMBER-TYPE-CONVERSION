n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  a=int(n)
  b=0
else:
  a=int(a)

p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
u=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
if a not in p:
 k=int(a/16)
 l=str(u[int(a%16)])
 while(k not in p):
  l=l+str(u[int(k%16)])
  k=int(k/16)
 l=l+str(u[int(k)])
 j=l[::-1]
else:
  j=str(u[a])

o=float("0."+b)
s=""
for _ in range(8):
  l=o*16
  k,d=str(float(l)).split(".")
  s=s+str(u[int(k)])
  o=float("0."+d)

  if o==0.0:
    break

print(j+"."+s)