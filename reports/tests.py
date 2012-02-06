"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from simpleapp.models import SimpleModel, SimpleReport
import os


class ReportTest(TestCase):
    def test_basic_addition(self):
        for i in xrange(0, 100):
            s = SimpleModel()
            s.name = i
            s.save()
        fname = SimpleReport.objects.all().make_report()
        os.remove(fname)


