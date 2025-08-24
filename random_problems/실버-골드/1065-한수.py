import sys
input = sys.stdin.readline

def hansu(N):
    # d_zero = [111,222,333,444,555,666,777,888,999]
    # d_one = [123,234,345,456,567,678,789,
    #          987,876,765,654,543,432,321,210]
    # d_two = [135,246,357,468,579,
    #          975,864,753,642,531,420]
    # d_three = [147,258,369,
    #            963,852,741,630]
    # d_four = [159,951,840]
    # d_all = d_zero + d_one + d_two + d_three + d_four

    result = 99

    if N < 100:
        return N
    elif 100 <=N and N < 1000:
        for i in range(100,N+1):
            digit_1000 = i // 1000
            digit_100 = (i - (digit_1000*1000))//100
            digit_10 = (i - (digit_1000 * 1000) - (digit_100 * 100)) // 10
            digit_1 = (i - (digit_1000 * 1000) - (digit_100 * 100) - (digit_10*10))//1
            if (digit_100 - digit_10) == (digit_10 - digit_1):
                result+=1
        return result
    else:
        return 144




N = int(input())
re = hansu(N)
print(re)

