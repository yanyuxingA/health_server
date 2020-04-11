import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import xlwt

from service.email.email import send_email
from users.models import Record
from users.serializers import HealthSerializer


class MainViewSet(viewsets.ModelViewSet):
    """
    用户健康状况记录
    """
    serializer_class = HealthSerializer

    def get_queryset(self):
        return Record.objects.filter().all()

    @action(methods=['post'], detail=False)
    def record(self, request):
        """用户健康状况报告接口"""
        serializer = HealthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user_name = data['user_name']
        user_age = data['user_age']
        user_temperature = data['user_temperature']
        user_address = data['user_address']

        Record.objects.create(user_name=user_name,
                              user_age=user_age,
                              user_temperature=user_temperature,
                              user_address=user_address)

        return Response('SUCCESS', status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False)
    def export(self, request):
        """健康记录汇总导出并发送"""
        # 创建一个文件对象
        wb = xlwt.Workbook(encoding='utf8')
        # 创建一个sheet对象
        sheet = wb.add_sheet('health-sheet')
        # 设置文件头的样式
        style_heading = xlwt.easyxf("""
                    font:
                        name Arial,
                        colour_index white,
                        bold on,
                        height 0xA0;
                    align:
                        wrap off,
                        vert center,
                        horiz center;
                    pattern:
                        pattern solid,
                        fore-colour 0x19;
                    borders:
                        left THIN,
                        right THIN,
                        top THIN,
                        bottom THIN;
                    """)

        # 写入文件标题
        sheet.write(0, 0, '姓名', style_heading)
        sheet.write(0, 1, '年龄', style_heading)
        sheet.write(0, 2, '体温', style_heading)
        sheet.write(0, 3, '地址', style_heading)
        sheet.write(0, 4, '时间', style_heading)
        sheet.write(0, 5, '人数', style_heading)

        records = Record.objects.filter(created_at__gte=(datetime.date.today() - datetime.timedelta(days=1))).filter(
            created_at__lte=datetime.date.today())
        # 写入数据
        data_row = 1
        for record in records:
            sheet.write(data_row, 0, record.user_name)
            sheet.write(data_row, 1, record.user_age)
            sheet.write(data_row, 2, record.user_temperature)
            sheet.write(data_row, 3, record.user_address)
            sheet.write(data_row, 4, record.created_at.strftime('%Y-%m-%d %H:%M:%S'))
            data_row = data_row + 1
        sheet.write(data_row, 5, data_row - 1)

        filename = 'health.xls'
        wb.save(filename)  # 保存文件

        res = send_email.send(filename)
        return res
