import zipfile

fileList = ["./Python/0920/test.bin", "./Python/0920/test.txt"]

# 파일 압축
# with zipfile.ZipFile("./Python/0920/test.zip", "w") as zf:
#     for file in fileList:
#         zf.write(file)
#         print(f"Add {file} to test.zip")

# 파일 압축 해제
zipfile.ZipFile("./Python/0920/test.zip", "w").extractall()