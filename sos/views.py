from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1> Welcome To My Django Project </h1>')
