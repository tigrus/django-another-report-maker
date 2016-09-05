from django.db import models
import datetime
import csv

class CSVError(Exception):
    pass

class ReportMaker(object):
    def __init__(self, objects=[]):
        self.objects = objects

    def make_report(self, name_map={}):
        rfields = self.objects.model.report_fields
        fname = self.objects.model.file_prefix % datetime.datetime.now().isoformat()
        writer = csv.writer(open(fname, 'w+'))
        writer.writerow([name_map.get(x, x) for x in rfields])


        for obj in self.objects:
            try:
                row = []
                for field in rfields:
                    fvalue = getattr(obj, field, '')
                    row.append(fvalue)
                writer.writerow(row)
            except Exception as e:
                raise CSVError((str(e), str(row)))
                # raise CSVError((e.message, str(row)))
        return fname


class ReportQuerySet(models.query.QuerySet):
    def make_report(self, name_map={}):
        r = ReportMaker(self)
        return r.make_report(name_map={})


class ReportManager(models.Manager):
    def get_query_set(self):
        return ReportQuerySet(self.model)

    # Alias for django 1.9
    def get_queryset(self):
        return self.get_query_set()
