def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if i==len(phone_book)-1:break
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


            
print(solution(["119", "97674223", "115524421"]))