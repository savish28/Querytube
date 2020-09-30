from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .tasks import youtube_search_keyword
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import status

class VideoList(ListAPIView):
	pagination_class = PageNumberPagination
	serializer_class = VideoSerializer
	queryset = Video.objects.all()

	def get_queryset(self):
		q = self.request.GET.get('query')
		if q is None:
			return Video.objects.all().order_by('-publish_date')
		return Video.objects.filter(query=q).order_by('-publish_date')

class Start(APIView):
	def get(self, request, format=None):
		query = Query.objects.all()
		serializer = QuerySerializer(query,many = True)
		return Response(serializer.data)
	def post(self, request, format=None):
		data = request.data
		serializer = QuerySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		youtube_search_keyword(data['query'],repeat = 60)
		return Response(serializer.data)
