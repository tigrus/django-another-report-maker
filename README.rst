django-another-report-maker
===========================

This is our idea, that we will develop, for  Django, allowing users to make csv reports as soon as possible.

We will add ``INSTALL`` instructions later.

Why we need another django report maker?
========================================

Most of report makers requires lot of settings to get it to work. We want just simple stupid solution that will work with proxy models and not managed models. 

Example of solution usage
=========================

Defenition of report easy as::

    from reports.models import ReportManager
    class MyCustomReport(MyModel):
        class Meta:
            proxy = True
            managed = False
        objects = ReportsManager()

        file_prefix = '/path/to/report/report_prefix_%s'
        report_fields = ['firstname', 'lastname', 'etc']

Usage is::

    filename = MyCustomReport.objects.filter(firstname='Vasya').make_report()
