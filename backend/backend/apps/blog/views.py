import django_filters
from rest_framework import generics

from .models import Posts
from .serializers import PostCreateSerializer, PostSerializer


class PostsListCreateAPIView(generics.ListCreateAPIView):
    """List posts."""

    class PostsFilter(django_filters.FilterSet):
        date = django_filters.DateFromToRangeFilter(field_name="date")
        search = django_filters.CharFilter(field_name="title", method="perform_search")

        # NOTE: In debug mode search filter is not working because of SQLite3 restrictions.

        def perform_search(self, queryset, name, value):
            """Search posts by title and content."""
            return queryset.filter(title__icontains=value) | queryset.filter(
                content__icontains=value
            )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCreateSerializer
        return PostSerializer

    queryset = Posts.objects.all()
    ordering_fields = ["date", "title"]
    filter_class = PostsFilter


class PostsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve/update/delete posts."""

    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    lookup_field = "slug"
