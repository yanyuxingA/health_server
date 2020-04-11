import configparser

from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from rest_framework.response import Response

from health_server import settings
from service.utils.path import get_config_path


class SendEmail(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config_path = get_config_path('email')
        config.read(config_path)
        self.subject = config.get('email', 'subject')
        self.html_content = config.get('email', 'html_content')
        self.to_email = config.get('email', 'to_email')

    def send(self, filename):

        msg = EmailMultiAlternatives(subject=self.subject, from_email=settings.EMAIL_HOST_USER, to=[self.to_email])
        msg.attach_alternative(self.html_content, 'text/html')
        try:
            msg.attach_file(filename)  # 添加附件
            msg.send()
        except:
            return Response('邮件发送失败了～', status=status.HTTP_400_BAD_REQUEST)
        return Response('SUCCESS')


send_email = SendEmail()