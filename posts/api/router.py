from rest_framework.routers import DefaultRouter
from posts.api.views import  PostModelViewSet

router_post=DefaultRouter()

# router_post.register('posts',PostViewSet,basename='posts')
router_post.register(prefix='posts', viewset=PostModelViewSet,basename='posts')