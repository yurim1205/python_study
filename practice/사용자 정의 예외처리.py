class BigNumError(Exception):
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자 입력: "))
    num2 = int(input("두 번째 숫자 입력: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))

except ValueError:
    print("한 자리 숫자만 입력 가능")
except BigNumError:
    print("오류발생. 한 자리 숫자만 입력 가능")
finally:
    print("감사합니다")