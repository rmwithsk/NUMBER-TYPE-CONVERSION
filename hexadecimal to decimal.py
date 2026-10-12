n=input('EN' +"\n")
try:
  a,b=n.split(".")
except ValueError:
  w=n
  d=""
else:
  w=a[::-1]
  d=b

hex=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

c=0
sum1=0
for i in w:
  l=hex.index(i)
  sum1=sum1+(num[l]*(16**c))
  c=c+1


c=1
sum2=0
for i in d:
  l=hex.index(i)
  sum1=sum1+(num[l]/(16**c))
  c=c+1

print(sum1+sum2)

  
