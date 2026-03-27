import collections

n = int(input())
ls = list(map(int, input().split()))
dq = collections.deque() #collections 모듈을 통해 덱 객체 생성

for i in range(n):
    dq.append((i + 1, ls[i])) #풍선의 번호와 풍선 안의 종이에 적혀 있는 수 리스트로 저장

list = [] #터진 풍선의 번호를 보여줄 리스트

while dq:
    a, b = dq.popleft() #첫 번째 풍선 터뜨리기
    list.append(a)

    if not dq:
        break
    if b > 0: #종이에 적혀있는 값만큼 이동
        dq.rotate(- b + 1)
    else:
        dq.rotate(-b)

print(*list)
