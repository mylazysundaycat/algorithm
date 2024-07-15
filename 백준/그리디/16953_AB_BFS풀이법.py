def dfs(current, target, depth):
    if current == target:
        return depth
    if current > target:
        return float('inf')

    # 두 가지 연산을 적용해 본다.
    res1 = dfs(current * 2, target, depth + 1)
    res2 = dfs(current * 10 + 1, target, depth + 1)

    return min(res1, res2)

def solve(A, B):
    result = dfs(A, B, 1)
    return result if result != float('inf') else -1

# 입력 받기
A, B = map(int, input().split())
print(solve(A, B))