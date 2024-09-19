import datetime

# 현재 시간을 출력
currentTime = datetime.datetime.now()
print(currentTime)

print(f"{currentTime.year}년 {currentTime.month}월 {currentTime.day}일 {currentTime.hour}시 {currentTime.minute}분 {currentTime.second}초")

# 문자열을 가지고 출력
print(currentTime.strftime("%Y-%m-%d %H:%M:%S"))