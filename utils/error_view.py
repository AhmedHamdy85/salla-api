from django.http import JsonResponse

def handeler404(request,exception):
    message = ('path no\'t found')
    response=JsonResponse(data={'error':message})
    response.status_code=404
    return response

def handeler500(request):
    message=('Internal server error')
    response= JsonResponse(data={
        'erorr':message
    })
    response.status_code=500
    return response