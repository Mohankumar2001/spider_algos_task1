n,r,x,y = map(int, input().split())
contestarr = list(map(int, input().split()))
csnarr = list(map(int, input().split()))
p = r
for i in range(n):
    if contestarr[i] ==1:
        if csnarr[i] == 1:
            r = r+x
        else:
            r = r-y
if r>p:
    print("promoted")
elif r<p:
    print("demoted")
else:
    print("no change")