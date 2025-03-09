N,K = map(int,input().split(' '))

def pac(x):
    mux = 1
    for i in range(1,x+1):
        mux = mux * i
    return mux

print(int(pac(N)/(pac(N-K) * pac(K))))
