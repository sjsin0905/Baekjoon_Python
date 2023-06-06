H, M, S = map(int, input().split())
time = int(input())

if time >= 3600:
    H += time // 3600
    time -= time // 3600 * 3600

M += time // 60
S += time % 60

if S >= 60:
    M += 1
    S -= 60
if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    if H // 24 > 1:
        H = H - (H // 24 * 24)
    else:
        H -= 24

print(f"{H} {M} {S}")
