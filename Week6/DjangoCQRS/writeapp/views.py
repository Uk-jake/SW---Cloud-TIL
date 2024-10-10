# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import status

# @api_view(['POST'])
# def bookAPI(request):
#    #전송된 데이터 읽기
#    data = request.data

#    #숫자로 변환
#    data['pages'] = int(data['pages'])
#    data['price'] = int(data['price'])

#    #Model 형태로 변환
#    serializer = BookSerializer(data=data)
#    if serializer.is_valid():
#        serializer.save() #테이블에 저장
#        #성공한 경우
#        return Response(serializer.data,
#                        status=status.HTTP_201_CREATED)
#    #실패한 경우
#    return Response(serializer.errors,
#                    status = status.HTTP_400_BAD_REQUEST)