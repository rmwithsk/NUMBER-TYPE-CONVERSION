def main(n):
      try:
        a,b=n.split(".")
      except ValueError:
        w=n
        d=""
      else:
        w=a
        d=b

      p=[0,1,2,3,4,5,6,7]
      u=["000","001","010","011","100","101","110","111"]
      st1=""
      for i in w:
        k=p.index(int(i))
        st1=st1+u[k]

      st2=""
      for i in d:
        k=p.index(int(i))
        st2=st2+u[k]

      return(st1+"."+st2)

if __name__ == "__main__":
    print(main(n=input('Enter an octal number: ' + "\n")))

  
