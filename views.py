from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page response")
    friends = ['ankit','ravi']
    return JsonResponse(friends,safe=False)