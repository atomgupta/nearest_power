{
import math
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(nearestPower(a,b))
        testcases-=1
        
if __name__=='__main__':
    main()
}


    
def nearestPower(a,b):
    t1=a
    t2=0
    temp=a
    while((b/t1>=a)):
        t1=t1*a
    t2=t1*a
    res=(t1 if(abs(t1-b)<abs(t2-b)) else t2)
    return res