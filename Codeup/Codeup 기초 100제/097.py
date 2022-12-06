# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 부모님과 함께 놀러간 영일이는
# 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
# (잉어, 붕어, 용 등 여러 가지가 적혀있다.)

# 격자판 생성
pan = []
h,w = map(int, input().split())
for i in range(h):
    pan.append([])
    for j in range(w):
        pan[i].append(0)

n = int(input())


for i in range(n):
    l,d,x,y = map(int, input().split())
    for j in range(l):
        if d == 0:
            pan[x-1][y-1] = 1
            y +=1
        else:
            pan[x-1][y-1] = 1
            x +=1

# 출력
for i in range(h):
    for j in range(w):
        print(pan[i][j], end=" ")
    print()
    
