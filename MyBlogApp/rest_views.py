from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from MyBlogApp.serializers import BlogSerializer


@csrf_exempt
@login_required
def rest_add_blog(request):
    if request.method == "POST":
        try:
            blog = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

        serializer = BlogSerializer(data=blog)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            status = 200
        else:
            data = serializer.errors
            status = 400

        content = JSONRenderer().render(data)
        return HttpResponse(content=content,
                            status=status,
                            content_type='application/json')
    else:
        return HttpResponse(status=404)

