H,M,S = map(int, input().split())
SS = int(input())

HOUR = (H +((M+((S+SS)//60))//60)) % 24
MIN = (M+((S+SS)//60)) % 60
SEC = (S+SS) % 60

print(HOUR,MIN,SEC)