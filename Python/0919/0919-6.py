import os.path
import glob
import sys

#print(dir(os.path))

#print(os.path.getatime("./python/0919/0919-6.py"))

# 현재 디렉토리의 파일 목록 출력
print(os.listdir("./"))

# glob는 확장자 패턴을 이용하게 되는데 보통 * 이나 ? 를 사용.
print(glob.glob("./python/0919/*.py"))

# 환경 변수 출력
#print(f"environs : {os.environ}")

# 운영체제 시스템 명령어 실행
os.system("ls -al")

# 운영 체제 이름 출력
print(f"os name : {os.name}")

print("모듈 찾는 순서 : ", sys.path )
print("디폴트 인코딩 : ", sys.getdefaultencoding())
print("참조 카운트 : ", sys.getrefcount(3))