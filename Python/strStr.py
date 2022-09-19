haystack = "hello"
needle = "ll"

def solution(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)

    return -1

print(solution(haystack, needle))