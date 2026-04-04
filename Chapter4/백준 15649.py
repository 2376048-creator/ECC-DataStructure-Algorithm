N, M = map(int, input().split())

arr = [] # 현재까지 만든 수열 저장
visited = [False] * (N + 1) # 숫자 사용 여부 확인

def find():
    if len(arr) == M:  # 수열 길이가 M이 되면 출력
        for x in arr:
            print(x, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            find() # 다음 자리 숫자 선택

            arr.pop() # 탐색이 끝나면 마지막 숫자 제거
            visited[i] = False # 다시 사용할 수 있도록 방문 해제

find()
