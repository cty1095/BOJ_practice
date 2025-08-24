A, B, C = map(int,input().split())
def conquer(A,B,C):
    con = (A * B) % C
    return con



def divide(a,b,c):
    if b == 1:
        return  (a % c)
    
    half = divide(a,b//2,c)
    half_x_half = conquer(half,half,c)
        
    if b % 2 == 0:
        return half_x_half
    else:
        return conquer(half_x_half, a%c , c)

re = divide(A,B,C)
print(re)

