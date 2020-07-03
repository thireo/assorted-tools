def ack(m,n):
    ans = 0
    if(m == 0):
        ans = n + 1
    elif(n == 0):
        ans = ack(m-1,1)
    else:
        ans = ack(m-1,ack(m,n-1))
    return ans

if __name__ == "__main__":
    import sys
    #sys.getrecursionlimit()
    #sys.setrecursionlimit(10000)
    for m in range(6):
        for n in range(6):
            print("ack(%d,%d):\t%d"%(m,n,ack(m,n)))