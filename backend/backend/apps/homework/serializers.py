from django.utils.timezone import datetime
from rest_framework import serializers

from ..core.models import Group, Klass, Quarter, Subject

# from ..core.lessons.serializers import LessonSerializer
from .models import Homework, HomeworkAttachment


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkAttachment
        fields = ["id", "file", "size"]


class AttachmentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new `HomeworkAttachment` instances."""

    def __init__(self, *args, **kwargs):
        self.homework_id = kwargs.pop("homework_id")
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        return HomeworkAttachment.objects.create(homework_id=self.homework_id, **validated_data)

    class Meta:
        model = HomeworkAttachment
        fields = ["file"]


class CreateHomeworkSerializer(serializers.ModelSerializer):
    """Serializer for creating new `Homework` instances."""

    attachments = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False), allow_empty=True, required=False
    )
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    klass = serializers.PrimaryKeyRelatedField(queryset=Klass.objects.all())
    date = serializers.DateField()

    def validate_date(self, value):
        if Quarter.get_quarter_by_date(value) is None:
            raise serializers.ValidationError("Домашнее задание нельзя задать на каникулы")
        return value

    def validate(self, data):
        print(data)
        if not data.get("content") and not data.get("attachments"):
            raise serializers.ValidationError("Укажите задание или прикрепите файлы")
        return data

    class Meta:
        model = Homework
        fields = ("content", "subject", "date", "attachments", "klass")

    def create(self, validated_data):
        attachments = validated_data.get("attachments")
        date: datetime = validated_data["date"]
        subject: Subject = validated_data["subject"]
        klass: Klass = validated_data["klass"]
        group, _ = Group.get_or_create(klass=klass, subject=subject)
        content: str = validated_data["content"]
        return Homework.add_homework(date, group, content, attachments)


class UpdateHomeworkSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())

    class Meta:
        model = Homework
        fields = ("content", "date", "group")

    def update(self, instance: Homework, validated_data):
        date = validated_data.pop("date") if "date" in validated_data else instance.lesson.date
        group = validated_data.pop("group") if "group" in validated_data else instance.lesson.group
        instance = super().update(instance, validated_data)

        instance.lesson.date = date
        instance.lesson.group = group
        instance.lesson.save()

        return instance


class HomeworkSerializer(serializers.ModelSerializer):
    """Serializer for listing `Homework` instances."""

    attachments = AttachmentSerializer(many=True, read_only=True)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    class Meta:
        model = Homework
        fields = ("id", "lesson", "content", "subject", "date", "attachments")
