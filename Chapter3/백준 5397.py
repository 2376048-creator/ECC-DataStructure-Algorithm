t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    s = input().strip() #입력 문자열 끝에 \n 제거

# 커서의 움직임이 중요하므로 커서를 중심으로 왼쪽과 오른쪽을 나눔
    left = []
    right = []

    for ch in s:
        if ch == '<':
            if left: # 왼쪽이 공백이 아니라면 왼쪽에서 오른쪽으로 문자 이동
                right.append(left.pop())
        elif ch == '>':
            if right: # 오른쪽이 공백이 아니라면 오른쪽에서 왼쪽으로 문자 이동
                left.append(right.pop())
        elif ch == '-':
            if left: # 문자 지우기
                left.pop()
        else:
            left.append(ch)

    for ch in left:
        print(ch, end="")
    
    for ch in reversed(right): # right는 커서 오른쪽 문자를 바로 꺼내기 위해 반대로 저장했으므로 뒤집어서 출력
        print(ch, end="")
    print()
