n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  w=n
  d=""
else:
  w=a
  d=b

p=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
u=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
st1=""
for i in w:
  k=p.index(i)
  st1=st1+u[k]

st2=""
for i in d:
  k=p.index(i)
  st2=st2+u[k]

print(st1+"."+st2)

  