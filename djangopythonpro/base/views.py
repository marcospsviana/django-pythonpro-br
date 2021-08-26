# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("""
    <html>
<head>
     <meta content='text/html'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h3>Olá django</h3>
</body>
</html>""")
