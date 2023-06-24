from django.conf import settings
from django.urls import path
from rest_framework import serializers, status, views
from rest_framework.response import Response


def get_settings_value(value: str, default: any):
    """Get value from Django project's settings."""
    return getattr(settings, value, default)


class DiaryxConfigSerializer(serializers.Serializer):
    """Serializer for DiaryX configuration."""

    school_name = serializers.CharField()
    school_n = serializers.CharField()
    school_full_name = serializers.CharField()
    plugins = serializers.ListField(child=serializers.CharField())


class DiaryxGetConfigAPIView(views.APIView):
    """API View for retrieving DiaryX configuration."""

    def get(self, request):
        data = {
            "school_name": settings.DIARYX_SCHOOL_NAME,
            "school_full_name": get_settings_value(
                "DIARYX_SCHOOL_FULL_NAME", settings.DIARYX_SCHOOL_NAME
            ),
            "plugins": get_settings_value("DIARYX_PLUGINS", ["__all__"]),
            "school_n": get_settings_value("DIARYX_SCHOOL_N", "X"),
        }

        serializer = DiaryxConfigSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


urlpatterns = [path("config", DiaryxGetConfigAPIView.as_view())]
