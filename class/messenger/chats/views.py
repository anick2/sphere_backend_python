from django.shortcuts import render
from django.http import JsonResponse

def main(request, chat_id):
    return JsonResponse({'status':'ok', 'chat_id':chat_id})
