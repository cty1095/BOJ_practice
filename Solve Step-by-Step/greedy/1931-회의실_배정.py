import sys

N = int(input())
meeting = []

for i in range(N):
    time = list(map(int,sys.stdin.readline().split()))
    meeting.append(time)

meeting.sort(key=lambda x: (x[1], x[0]))



cnt = 0
endtime = 0
# ans = []
for time in meeting:
    if time[0] >= endtime:
        # ans.append(time)
        cnt += 1
        endtime = time[1]

print(cnt)
# print(ans)