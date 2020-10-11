from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from busking_auth.views import login_view
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', csrf_exempt(login_view)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("upload/", include("upload.urls", namespace="upload"))
]
