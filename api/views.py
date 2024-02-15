import os
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView
from TestGenerate.image_filters import image_filter
from TestGenerate.text_filter import edit_test
from api.models import Document, GenerateTest
from api.serializers import DocumentSerializer, GenerateTestSerializer, GeneratePDFSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


class HelloApiView(ListAPIView):
    def get(self, request):
        return Response({'message': 'Welcome to CamTest!'})


class SavedTest(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def post(self, request):
        global files, files_, images
        document = self.serializer_class(data=request.data)
        document.is_valid(raise_exception=True)
        document.save()

        # Get the saved document object
        saved_document = document.instance

        input_loc = f"/home/nazarbek/CamTest-admin{saved_document.document.url}"
        output_loc = f"/home/nazarbek/CamTest-admin/media/database_images"
        image_filter(input_loc, output_loc)
        data = edit_test(f"/home/nazarbek/CamTest-admin/{saved_document}")

        for root, dirs, files in os.walk(output_loc):
            images = []
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_path = os.path.join(root, file)
                    with open(image_path, 'rb') as img_file:
                        image = Image.open(img_file)
                        image_file = SimpleUploadedFile(
                            name=file,
                            content=img_file.read(),
                            content_type='image/jpeg' if file.endswith(".jpg") else 'image/png'
                        )
                        images.append(image_file)
                    os.remove(image_path)
        sorted_images = sorted(images, key=lambda x: x.name)
        print('sorted images >>> ', sorted_images)
        for i in range(len(data)):
            if len(sorted_images) > i:
                question = data[i]
                image = sorted_images[i]
                answer = data[i].split('//')[1]
            else:
                question = data[i]
                image = ''
                answer = data[i].split('//')[1]
            GenerateTest.objects.create(
                question=question,
                image=image,
                answer=answer
            )
        return Response({'success': True})


class GeneratePDF(ListCreateAPIView):
    serializer_class = GeneratePDFSerializer

    def post(self, request, lan, fan1, fan2, quantity):
        pass
