def solution(word):

    word.strip()
    word = word.split()

    return len(word[-1])

print(solution("   fly me   to   the moon  "))