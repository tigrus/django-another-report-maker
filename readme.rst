django-another-report-maker
===========================

This is my idea, that we will develop, for  Django_ *framework*, **allowing users to make csv reports as soon as possible**.

We will add ``INSTALL`` instructions later.

Why we need another django report maker?
=======================================

Most of report makers requires lot of settings to get it to work. We want just simple stupid solution that will work with proxy models and not managed models. 

Example of solution usage
=========================

Defenition of report must be easy as:

    class MyCustomReport(MyModel, ReportMaker):
        filename = '/path/to/report'
        report_fields = ['firstname', 'lastname', 'etc']

We assume that you will build report on top of the postgresql views or simple tables. No heavy work on slow django-orm level.

In code, Report will be used as:
    
    def my_report(request):
       r = MyCustomReport() 

       #We can get filename as property
       r.report_filename

       #We can get report content as property
       r.report_content

       return HttpResponse(r.report_content)
