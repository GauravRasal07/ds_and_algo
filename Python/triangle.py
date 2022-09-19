def solution(t, ind, level, res):
    # print(level, res, ind)  
    if level == len(t):
        # res.append(ind)
        print("Last level:", res)
        return 0

    if res[level][ind] != float('inf'):
        return res[level][ind]

    print("Level:", level, "Ind:", ind, "T:", solution(t, ind, level + 1, res))
    print("Level:", level, "Ind:", ind, "T:", solution(t, ind + 1, level + 1, res))
    res[level][ind] = min(solution(t, ind, level + 1, res), solution(t, ind + 1, level + 1, res))
    return res[level][ind]

    
    

# t = [[-1],[2,3],[1,-1,-3]]
# t = [[-10]]
t =[[2],[3,4],[6,5,7],[4,8,1,3]]

res = []

for i in range(len(t)):
    res.append([float('inf')] * len(t[i]))

print(res)
print(solution(t, 0, 0, res))
print(res)