import collections

n, K = map(int, input().split())
dq = collections.deque(range(1, n+1))


print("<", end="")
while dq:
    dq.rotate(-(K-1)) # K번째 사람이 배열 앞으로 오도록 회전
    if len(dq) == 1: # 제거되는 사람들 순서대로 출력
        print(dq.popleft(), end="") 
    else:
        print(dq.popleft(), end=", ") 

print(">")
