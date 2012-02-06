from django.db import models
import datetime
import csv


class ReportMaker(object):
    def __init__(self, objects=[]):
        self.objects = objects

    def make_report(self):
        rfields = self.objects.model.report_fields
        fname = self.objects.model.file_prefix % datetime.datetime.now().isoformat()
        writer = csv.writer(open(fname, 'w+'))
        writer.writerow(rfields)

        for obj in self.objects:
            row = []
            for field in rfields:
                fvalue = getattr(obj, field, '')
                row.append(fvalue)
            writer.writerow(row)
        return fname


class ReportQuerySet(models.query.QuerySet):
    def make_report(self):
        r = ReportMaker(self)
        return r.make_report()


class ReportManager(models.Manager):
    def get_query_set(self):
        return ReportQuerySet(self.model)
