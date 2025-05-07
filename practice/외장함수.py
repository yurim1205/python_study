# glob: 경로 내의 폴더 / 파일 목록 조회
import glob
print(glob.glob("*.py"))

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 출력

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M"))

import datetime
print("오늘 날짜는 ",datetime.date.today())

today=datetime.date.today()
td = datetime.timedelta(days=70)
print("70일 뒤는",today+td)