N = int(input())
listA = list(map(int,input().split()))
op = list(map(int,input().split()))

# a = + , b = - , c = * , d = //
op_dict = {"a" : op[0], "b" : op[1], "c" : op[2] , "d" : op[3]}


def pre():
    INF = 10**9 
    max_value = -float('inf')
    min_value = float('inf')
    
    def dfs(depth,value):
        nonlocal max_value , min_value

        if depth == N-1:    
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
            return max_value, min_value
        
        next = listA[depth + 1]
   
        for key in op_dict:
            if op_dict[key] > 0:
                op_dict[key] -= 1 

                if key =="a":
                    tmp = value + next
                elif key == "b":
                    tmp = value - next
                elif key == "c":
                    tmp = value * next
                elif key == "d":
                    if value < 0:
                        tmp = -(-value // next)
                    else:
                        tmp = value // next

                dfs(depth+1, tmp)
                op_dict[key] += 1 


    dfs(0,listA[0])
    
    
    return max_value, min_value

max1, min1 =pre()
print(max1)
print(min1)