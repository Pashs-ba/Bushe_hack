from pathlib import Path

from backend.apps.core.models import Control, Group, Klass, Quarter, Subject
from django.test import TestCase
from django.utils.timezone import datetime, timedelta

from ..models import Homework


class TestHomework(TestCase):
    """Test cases for homework module."""

    HW_CONTENT = "Выполнить задания на языке программирования Pascal"
    HW_DATE = f"{(datetime.now() + timedelta(days=2)):%Y-%m-%d}"
    HW_FILE_PATH = Path(__file__).resolve().parent / "files" / "task_example.jpg"

    def setUp(self) -> None:
        """Populate database with some data that is needed to add homework."""
        subject = Subject.objects.create(name="ИКТ")
        klass = Klass.objects.create(name="11з")
        klass.subjects.add(subject)

        Control.objects.create(name="Классная работа", weight=1)

        Quarter.objects.create(
            number=1,
            begin=(datetime.now() - timedelta(days=7)),
            end=(datetime.now() + timedelta(days=7)),
        )

        self.group = Group.objects.create(subject=subject, klass=klass)

    def test_homework_create_and_detail(self):
        """Test adding a new task and attaching a file to it."""
        with open(self.HW_FILE_PATH, "rb") as fp:
            response = self.client.post(
                "/api/homework",
                {
                    "attachments": [fp],
                    "group": self.group.id,
                    "content": self.HW_CONTENT,
                    "date": self.HW_DATE,
                },
            )

        self.assertEqual(response.status_code, 201)

        # Get the created instance
        hw_id = response.json().get("id")
        created = Homework.objects.get(id=hw_id)

        # Check that the file is attached
        self.assertEqual(created.attachments.count(), 1)

        response = self.client.get(f"/api/homework/{hw_id}")
        self.assertEqual(response.status_code, 200)

    def test_homework_update(self):
        hw_obj = Homework.add_homework(self.HW_DATE, self.group, self.HW_CONTENT)

        NEW_HW_DATE = datetime.date(datetime.now()) + timedelta(days=5)
        NEW_HW_CONTENT = 'Read "Crime and punishment"'

        response = self.client.patch(
            f"/api/homework/{hw_obj.id}",
            {
                "content": NEW_HW_CONTENT,
                "date": f"{(NEW_HW_DATE):%Y-%m-%d}",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

        hw_obj.refresh_from_db()
        self.assertEqual(hw_obj.date, NEW_HW_DATE)
        self.assertEqual(hw_obj.content, NEW_HW_CONTENT)

        hw_obj.delete()

    def test_homework_list(self):
        response = self.client.get("/api/homework")
        self.assertEqual(response.status_code, 200)
