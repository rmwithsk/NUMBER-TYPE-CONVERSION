n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  w=n
  d=""
else:
  w=a
  d=b

m=int(len(w)%4)
n=int(len(d)%4)

if m>0:
  w="0"*(4-m)+w 

if n>0:
  d=d+"0"*(4-n)

p=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
u=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

s1, c= "", 0
for _ in range(int(len(w)/4)):
  o=w[c:c+4]
  s1=s1+p[u.index(o)]
  c=c+4

s2, c= "", 0
for _ in range(int(len(d)/4)):
  o=d[c:c+4]
  s2=s2+p[u.index(o)]
  c=c+4

print(s1+"."+s2)