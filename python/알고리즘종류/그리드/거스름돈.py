n = 1260  # 현재금액
count = 0

array = [500, 100, 50, 10]  # 화폐단위 큰 단위부터

for coin in array:
    count += n//coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    print(count)

print(coin)
