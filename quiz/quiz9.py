class SoldOutError(Exception):
      pass

chicken = 10
waiting = 1

while(True):
        try:
            print("남은 치킨: {0}".format(chicken))
            order = int(input("치킨 몇 마리 주문하시겠습니까?"))

            if order> chicken:
                print("재료 소진")
            elif order <= 0:
                  raise ValueError
            else:
                print("[대기번호 {0}] {1}마리 주문 완료됨" \
                    .format(waiting,order))
                waiting += 1
                chicken -= order

            if chicken == 0:
                  raise SoldOutError
                        
        except ValueError:
                print("잘못된 값을 입력하였습니다.")
        except SoldOutError:
              print("재고 소진")
              break