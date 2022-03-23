def solution(s):
    answer = []
    for i in range(len(s)):
        cnt=0
        for j in range(len(s)):
            print(s[j])
            if s[j]==s[:i]:
                cnt+=1
        answer.append(str(cnt)+s[i])


    return answer

print(solution("aabbaccc"))