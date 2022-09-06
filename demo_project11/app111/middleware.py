

# class UnderMaitenance(object):
#     def __init__(self, get_response):
#         """
#         One-time configuration and initialisation.
#         """
#         self.get_response = get_response
#
#     def __call__(self, request):
#         """
#         Code to be executed for each request before the view (and later
#         middleware) are called.
#         """
#         response = self.get_response(request)
#         return "AGSGADGADHGD"

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
         self.get_response=get_response

    def __call__(self,request):
      return HttpResponse('<h1>Currently Application under maintenance...try after 2 days!!!')