l1=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
l2=[1,1,1,1,1,1,1,1]
l3=[1,1,1,1,1,2,3,1,1,1,1,1]
l4=[1,2,4,4,5,7,2,1,1,4,2,2]
l5=[0,1,2,3,4,5,6,7,8]
l6=[1,2,5,5,5,6,6,6,5,5,5,6,6,6,7,7,7,1,2,4,4,4,44,4,4]
l7=['a','b','d','d','d','d','e','e','f','g','a','a','aa','a','a']
def fun(l):
    l.append([])
    l1=[]
    i=0
    while(i<len(l)):

        if type(l[i]) == type(l):
            break
        elif l[i] == l[i + 1]:
                for j in range(i+2,len(l)):
                    if l[i]==l[j]:
                        pass
                    else:
                        q=j
                        break
                s=l[i:q]
                l1.append(s)
                m=len(s)
                i=i+m
        else:
                l1.append(l[i])
                i=i+1
        
    print(l1)

fun(l1)
fun(l2)
fun(l3)
fun(l4)
fun(l5)
fun(l6)
fun(l7)

