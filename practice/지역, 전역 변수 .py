bread = 10

def checkpoint(customer):
    global bread # 전역 변수 사용
    bread = bread-customer
    print("[함수 내] 남은 빵: {0}".format(bread))

def checkpoint_re(bread, customer):
    bread = bread - customer
    print("[함수 내] 남은 빵: {0}".format(bread))
    return bread

print("전체 빵: {0}".format(bread)) 
# checkpoint(2)
bread = checkpoint_re(bread, 2) 
print("남은 빵: {0}".format(bread)) 