from django.urls import path

from api.views.cam_test_user import CamTestUserView
from api.views.download_file import DownloadFileAPIView
from api.views.generate_test import GenerateTest
from api.views.upload_document import UploadDocumentView
from api.views.upload_file_with_image import UploadFileWithImageView
from api.views.languages import LanguagesView
from api.views.subjects import SubjectsView

urlpatterns = [
    path('subjects', SubjectsView.as_view(), name='subject'),  # mobile
    path('upload-file', UploadDocumentView.as_view(), name='upload_file'),  # admin
    path('upload-file-with-image', UploadFileWithImageView.as_view(), name='upload_file_with_image'),  # admin
    path('generate-test', GenerateTest.as_view(), name='generate_test'),  # mobile
    path('languages', LanguagesView.as_view(), name='languages'),  # mobile
    path('download/<int:user_id>', DownloadFileAPIView.as_view(), name='download_user_file'),  # mobile
    path('camtest-user', CamTestUserView.as_view(), name='camtest_user'),  # mobile
]
