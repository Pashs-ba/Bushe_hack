from django.test import TestCase

from ..models import Control


class TestControls(TestCase):
    def setUp(self) -> None:
        Control.objects.create(name="Классная работа", weight=1)

    def testControlDefault(self):
        """Test default control retrieval."""
        ctrl = Control.get_default()
        self.assertNotEqual(ctrl, None)
