kia = ["kia0", "kia1", "kia2", "kia3", "kia4"]
hanwa = ["hanwa0", "hanwa1", "hanwa2", "hanwa3", "hanwa4"]
ssg = ["ssg0", "ssg1", "ssg2", "ssg3", "ssg4"]


# 배열 저장 시에는 list보다 dict가 더 효율적이다.
# 각 배열의 특징을 같이 저장하는 것이 더 유용함.
# kbo = [kia, hanwa]
dict1 = {"team" : "기아", "data" : kia}
dict2 = {"team" : "한화", "data" : hanwa}
dict3 = {"team" : "SSG", "data" : ssg}


kbo = [dict1, dict2, dict3]

# for idx, data in enumerate(kbo):
#     if idx == 0:
#         print("KIA 타자 명단", end=" ")
#     elif idx == 1:
#         print("한화 타자 명단", end=" ")
    
#     for player in data:
#         print(player, end = " ")    

for data in kbo:
    print(f"{data['team']}의 타자 명단 : ", end=" ")
    for player in data["data"]:
        print(player, end=" ")
    print()