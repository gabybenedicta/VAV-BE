from firebase_admin import auth
from django.http import JsonResponse
from rest_framework import status

class VerifyTokenMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if 'HTTP_AUTHORIZATION' in request.META:
			try:
				id_token = request.META['HTTP_AUTHORIZATION']
				decoded_token = auth.verify_id_token(id_token)
				uid = decoded_token['uid']
			except auth.RevokedIdTokenError:
				message = {'message':"Token has expired"}
				return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
			except auth.InvalidIdTokenError:
				message = {'message':"Token in invalid"}
				return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
			if uid:
				return self.get_response(request)
			else:
				message = {'message':"Unauthorised User"}
				return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
		else:
			message = {'message':"Unauthorised User"}
			return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
