import 모듈

모듈.price(1)
모듈.price_morning(4)
모듈.price_soldier(5)

import 모듈 as md
md.price_morning(2)

from 모듈 import *
price_morning(4)
price(2)

from 모듈 import price, price_morning
price(5)
price_morning(2)

from 모듈 import price_morning as pm
pm(5)