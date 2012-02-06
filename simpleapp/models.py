from django.db import models
from reports.models import ReportManager

# Create your models here.
class SimpleModel(models.Model):
    name = models.CharField(max_length=250)

class SimpleReport(SimpleModel):
    class Meta:
        proxy = True
        managed = False

    report_fields = ['name', 'custom_field']
    file_prefix = '/projects/simple_%s.csv'
    objects = ReportManager()

    @property
    def custom_field(self):
        return 'hi'
