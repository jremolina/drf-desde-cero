from django.urls import path, include
from .import views
# from .api.views import PostApiView
# from .api.views import PostViewSet
from posts.api.router import router_post


urlpatterns=[
    path('', views.HelloWorld.as_view()),
    # path('api/posts/', PostApiView.as_view())
    path('api/', include(router_post.urls))
   

]