def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    wear = {}
    for _, val in clothes:
        wear[val] = wear.get(val, 0) + 1
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for val in wear:
        answer *= wear[val] + 1
        print(answer)

    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
