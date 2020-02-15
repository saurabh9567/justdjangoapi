from rest_framework.views import APIView
from rest_framework.response import Response
from .sereializers import PostSerializer
from .models import Post


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)














# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     return JsonResponse(data)