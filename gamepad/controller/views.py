from django.shortcuts import redirect, render
from .models import GamePad
from .serializer import GamePadSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response



def index(request):
    gamepad = GamePad.objects.all()

    serializer = GamePadSerializer()

    if request.method == 'POST':
        serializer = GamePadSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
        return redirect('/')

    context = {'gamepad':gamepad, 'serializer':serializer}

    return render(request, 'controller/index.html', context)

