from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail


def mail(request):
    send_mail('One Django send-mail test',             # 主题
              'Congratulations! you got one lucky email!',     # 正文
              '936233993@qq.com',         # 发件人
              ['793166729@qq.com'],       # 收件人
              fail_silently=False)
    return HttpResponse('邮件发送成功，收不到就去垃圾箱找找吧！')