from firebase_admin import auth
from django.http import JsonResponse
from rest_framework import status

class VerifyTokenMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if 'HTTP_AUTHORIZATION' in request.META:
			id_token = request.META['HTTP_AUTHORIZATION']
			decoded_token = auth.verify_id_token(id_token)
			uid = decoded_token['uid']
			if uid:
				return self.get_response(request)
			else:
				message = {'message':"Unauthorised User"}
				return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
		else:
			message = {'message':"Unauthorised User"}
			return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
		
