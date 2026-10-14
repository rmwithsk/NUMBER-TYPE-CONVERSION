def main(n):
    try:
      a,b=n.split(".")
    except ValueError:
      w=n
      d=""
    else:
      w=a
      d=b

    m=int(len(w)%3)
    n=int(len(d)%3)

    if m>0:
      w="0"*(3-m)+w 

    if n>0:
      d=d+"0"*(3-n)

    p=["0","1","2","3","4","5","6","7"]
    u=["000","001","010","011","100","101","110","111"]

    s1, c= "", 0
    for _ in range(int(len(w)/3)):
      o=w[c:c+3]
      s1=s1+p[u.index(o)]
      c=c+3

    s2, c= "", 0
    for _ in range(int(len(d)/3)):
      o=d[c:c+3]
      s2=s2+p[u.index(o)]
      c=c+3

    print(s1+"."+s2)

if __name__ == "__main__":
    n=input('EN' +"\n")
    main(n)