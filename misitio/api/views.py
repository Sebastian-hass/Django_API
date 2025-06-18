from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        #Obtiene el titulo del query parameter (si no hay, devuelve un string vacio)
        title = request.query_params.get("title", "")

        if title:
            #Filtramos el queryset según el titulo
            blog_posts = BlogPost.objects.filter(title_icontains=title)
        else:
            #si no se provee de un titulo, devuelve todo el blog post
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)