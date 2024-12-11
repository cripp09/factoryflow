from celery import shared_task
import cv2
from .models import Polutushi
from datetime import datetime
import os

@shared_task
def capture_image_from_rtsp(**queryset):
    """Создание объекта "Полутуши", со скрином из ip камеры и соответствующим весом """
    rtsp_url = queryset.get('rtsp_url')
    weight_request = queryset.get('weight')
    image_link = ''
    cap = cv2.VideoCapture(rtsp_url)
    ret, frame = cap.read()
    if ret:
        current_date = datetime.now()
        formatted_date = current_date.strftime("/%Y/%m/%d")
        formatted_time = current_date.strftime("%H_%M_%S")
        folder_path = f'media/polutushi{formatted_date}'
        file_name = f'{formatted_time}_{weight_request}'
        os.makedirs(folder_path, exist_ok=True)
        image_link_relative = f'{folder_path}/{file_name}.jpeg'
        image_link = f'polutushi{formatted_date}/{file_name}.jpeg'
        cv2.imwrite(image_link_relative, frame)
        cap.release()
    else:
        print("Ошибка при захвате кадра.")
        cap.release()
    Polutushi.objects.create(weight=weight_request, image=image_link or '' )