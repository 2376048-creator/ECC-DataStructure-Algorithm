import collections

n, m = map(int, input().split())
ls = list(map(int, input().split())) # 뽑아내려고 하는 원소의 위치 리스트
dq = collections.deque(range(1, n+1)) #collections 모듈을 통해 덱 객체 생성
count = 0

for i in ls:
    idx = dq.index(i) #뽑아내려고 하는 원소의 위치 찾기
    if idx <= len(dq)//2: #위치가 중간보다 왼쪽에 위치하면 왼쪽으로 회전
         dq.rotate(-idx) #왼쪽으로 위치만큼 회전
         count += idx
    else:
        dq.rotate(len(dq) - idx) #오른쪽으로 전체에서 위치의 차이만큼 회전
        count += len(dq) - idx
    dq.popleft()

print(count)
