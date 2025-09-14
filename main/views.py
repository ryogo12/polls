from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    question_list = [
             "ゲームは好きですか",
             "Mincraftは好きですか",
             "こんにちは",
       ]
    context = {
          "question_list": question_list,
          "is_polled":False,
          "polled_msg": "投票してくれてありがとう",
          "not_polled_msg": "投票してください泣",
    }
    return render(request, "main/index.html", context)