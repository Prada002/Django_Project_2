from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .models import DataList, Depart
from .serializers import DataListSerializer ,DepartSerializer

@permission_classes((AllowAny,))
class DataLists(APIView):
    def get(self, request):
        data = DataList.objects.all()
        serializer = DataListSerializer(data, many=True)
        return Response({'message': 'data retrieved', 'Status': 'Pass', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DataListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data created', 'Status': 'Pass'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Validation failed', 'Status': 'Fail', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = DataList.objects.get(pk=pk)
        except DataList.DoesNotExist:
            return Response({'message': 'Data not found', 'Status': 'Fail'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataListSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data updated', 'Status': 'Pass'}, status=status.HTTP_200_OK)
        return Response({'message': 'Validation failed', 'Status': 'Fail', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            data = DataList.objects.get(pk=pk)
        except DataList.DoesNotExist:
            return Response({'message': 'Data not found', 'Status': 'Fail'}, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response({'message': 'data deleted', 'Status': 'Pass'}, status=status.HTTP_204_NO_CONTENT)

    
    
    
@permission_classes((AllowAny,))
class Department(APIView):
    def get(self, request):
        data = Depart.objects.all()
        serializer = DepartSerializer(data, many=True)
        return Response({'message': 'data retrieved', 'Status': 'Pass', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data created', 'Status': 'Pass'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Validation failed', 'Status': 'Fail', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data_id = request.data.get("id", "")
        try:
            data = Depart.objects.get(id=data_id)
        except Depart.DoesNotExist:
            return Response({'message': 'Data not found', 'Status': 'Fail'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data updated', 'Status': 'Pass'}, status=status.HTTP_200_OK)
        return Response({'message': 'Validation failed', 'Status': 'Fail', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data_id = request.data.get("id", "")
        try:
            data = Depart.objects.get(id=data_id)
        except Depart.DoesNotExist:
            return Response({'message': 'Data not found', 'Status': 'Fail'}, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response({'message': 'data deleted', 'Status': 'Pass'}, status=status.HTTP_204_NO_CONTENT)

