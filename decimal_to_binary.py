n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  a=int(n)
  b=0
else:
  a=int(a)
  b=int(b)

if a not in [0,1]:
 k=int(a/2)
 l=str(int(a%2))
 while(k!=1):
  l=l+str(int(k%2))
  k=int(k/2)
 l=l+str(int(k))
 j=l[::-1]
elif a==0:
  j="0"
elif a==1:
  j="1"

o=float("0."+str(b))
s=""
for _ in range(8):
  l=o*2
  k,d=str(float(l)).split(".")
  s=s+k
  o=float("0."+d)

  if o==0.0:
    break

print(j+"."+s)