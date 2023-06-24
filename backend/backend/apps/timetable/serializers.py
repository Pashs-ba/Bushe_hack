from backend.apps.core.subjects import SubjectSerializer
from rest_framework import serializers

from .models import Bell, TimetableLesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for TimetableLesson model."""

    n = serializers.IntegerField(source="number.n")
    start = serializers.TimeField(source="number.start")
    end = serializers.TimeField(source="number.end")
    subject = SubjectSerializer()

    class Meta:
        model = TimetableLesson
        fields = ["n", "start", "end", "subject", "classroom", "id", "day"]


class BellSerializer(serializers.ModelSerializer):
    """Serializer for `Bell` model."""

    class Meta:
        model = Bell
        fields = ["id", "n", "start", "end"]


class CreateLessonsSerializer(serializers.ModelSerializer):
    """Serializer for editing timetable."""

    n = serializers.IntegerField()

    class Meta:
        model = TimetableLesson
        fields = ["n", "classroom", "day", "klass", "subject"]

    def create(self, validated_data):
        """Create lessons."""
        n = validated_data["n"]

        # Get or create a bell for the lesson
        bell = Bell.get_or_generate(n=n)

        try:
            lesson = TimetableLesson.objects.get(
                number=bell,
                day=validated_data["day"],
                klass=validated_data["klass"],
                subject=validated_data["subject"],
            )
            lesson.classroom = validated_data["classroom"]
            lesson.save()
        except TimetableLesson.DoesNotExist:
            lesson = TimetableLesson.objects.create(
                number=bell,
                day=validated_data["day"],
                klass=validated_data["klass"],
                subject=validated_data["subject"],
                classroom=validated_data["classroom"],
            )
        return lesson


class DeleteLessonSerializer(serializers.ModelSerializer):
    """Serializer for deleting lessons."""

    n = serializers.IntegerField()

    class Meta:
        model = TimetableLesson
        fields = ["n", "day", "klass", "subject"]
