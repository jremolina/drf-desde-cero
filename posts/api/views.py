from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer


# class PostApiView(APIView):
# ====================== USO DE SERIALIZADORES ==============

#     def get(self, request):
#         # posts = Post.objects.all()
#         # posts = [posts.title for posts in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(),many=True)
#         return Response(status=status.HTTP_200_OK,data =serializer.data)  

#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED,data=serializer.data)

#         # Post.objects.create(title=request.POST['title'],description=request.POST['description'],order=request.POST['order'])
#         # return self.get(request)


# ====================== USO DE ViewSet ==============

# class PostViewSet(ViewSet):    
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(),many=True)
#         return Response(status=status.HTTP_200_OK,data =serializer.data)

#     def retrieve(self,request,pk:int):
#         post = PostSerializer(Post.objects.get(pk=pk))        
#         return Response(status=status.HTTP_200_OK,data=post.data)    

#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED,data=serializer.data)


# ====================== USO DE ModelViewSet =========================

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


