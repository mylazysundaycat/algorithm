
x = int(input())
def goToOne(x):
    if x==1: return 1
    return min(
        (goToOne(x/5) if x%5==0 else 0)+1,
        (goToOne(x/3) if x%3==0 else 0)+1,
        (goToOne(x/2) if x%2==0 else 0)+1,
        goToOne(x-1)+1
    )

print(goToOne(x))
