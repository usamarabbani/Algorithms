'''def stairs(n):
    if len(n)=2:
        return n

    first, second = 1,2
    for i in range(len(n)):
        third=first+second
        first=second
        second=third

    return second'''
def stairs(n):


    memoized=[]
    memoized.append(1)
    memoized.append(2)
    for i in range(2,n):
        memoized.append(0)
        memoized[i]=memoized[i-1] +memoized[i-2]

    return memoized[n-1]


