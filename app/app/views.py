from django.http import HttpResponse


def index(request):
    variable = {
        'title': 'Hello World',
        'content': 'This is the content of the page',
    }

    variable['new_content'] = 'This is the new content of the page'

    
    return HttpResponse('test page for django')