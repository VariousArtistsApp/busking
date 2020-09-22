from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from user.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', csrf_exempt(login_view)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
