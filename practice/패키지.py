# import travel.thailand
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from ~ import 구문에서는 모듈,패키지,클래스,함수 다 import가능
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to=vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# trip_to=thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(thailand))