from django.test import TestCase

from backend.apps.timetable.models import Bell, TimetableLesson
from ..core.models import Klass, Plugin, Subject
import json
from rest_framework import status


TEST_SUBJECTS = [
    "Алгебра",
    "Геометрия",
    "Информатика",
    "Литература",
]


class TimetableTests(TestCase):
    """Timetable tests."""

    def setUp(self):
        """Create a klass, and some subjects."""
        self.subjects = []
        for subject in TEST_SUBJECTS:
            self.subjects.append(Subject.objects.create(name=subject))
        self.klass = Klass.objects.create(name="10З")
        self.klass.subjects.set(self.subjects)
        Plugin.objects.create(name="timetable")

    def test_timetable_edit(self):
        """Test editing a timetable."""
        # Delete all lessons.
        TimetableLesson.objects.all().delete()

        response = self.client.post(
            "/api/timetable/bulk-create/",
            json.dumps(
                [
                    {
                        "n": 1,
                        "classroom": "206",
                        "day": 1,
                        "klass": self.klass.id,
                        "subject": self.subjects[0].id,
                    },
                    {
                        "n": 2,
                        "classroom": "203",
                        "day": 1,
                        "klass": self.klass.id,
                        "subject": self.subjects[1].id,
                    },
                    {
                        "n": 3,
                        "classroom": "410",
                        "day": 1,
                        "klass": self.klass.id,
                        "subject": self.subjects[2].id,
                    },
                    {
                        "n": 4,
                        "classroom": "505",
                        "day": 1,
                        "klass": self.klass.id,
                        "subject": self.subjects[3].id,
                    },
                ]
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that all lessons were created.
        self.assertEqual(TimetableLesson.objects.count(), 4)

        # Bells should be also created.
        self.assertEqual(Bell.objects.count(), 4)

    def test_timetable_retrieve(self):
        """Test retrieving a timetable."""
        response = self.client.get(f"/api/timetable/{self.klass.id}")
        self.assertEqual(response.status_code, 200)
