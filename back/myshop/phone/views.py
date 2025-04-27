from phone.models import Brand, Camera, Color, Phone, So, Screen_resolution
from phone.serializers import PhoneSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

class PhoneListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data)
    
class PhoneNewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            phone = Phone()

            if request.data.get('brand'):
                try:
                    phone.brand = Brand.objects.get(brand=request.data['brand'])
                except ObjectDoesNotExist:
                    return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)

            if request.data.get('camera'):
                camera = Camera.objects.filter(camera_name=request.data['camera']).first()
                if camera:
                    phone.camera = camera
                else:
                    return Response({"error": "Camera not found"}, status=status.HTTP_404_NOT_FOUND)

            if request.data.get('screen_resolution'):
                try:
                    phone.screen_resolution = Screen_resolution.objects.get(resolution=request.data['screen_resolution'])
                except ObjectDoesNotExist:
                    return Response({"error": "Screen resolution not found"}, status=status.HTTP_404_NOT_FOUND)


            if request.data.get('color'):
                color = Color.objects.filter(color=request.data['color']).first()
                if color:
                    phone.color = color
                else:
                    return Response({"error": "Color not found"}, status=status.HTTP_404_NOT_FOUND)

            if request.data.get('so'):
                so_data = request.data['so'].split(',')
                if len(so_data) == 2:
                    so_name = so_data[0].strip()
                    firmware = so_data[1].strip()

                    so = So.objects.filter(so=so_name).first()
                    if so:
                        phone.so = so
                        phone.firmware = firmware
                    else:
                        return Response({"error": "S.O. not found"}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({"error": "Invalid format for S.O. and firmware"}, status=status.HTTP_400_BAD_REQUEST)

            phone.model = request.data.get('model', '')
            phone.ram = request.data.get('ram', '')
            phone.battery = request.data.get('battery', '')
            phone.price = request.data.get('price', 0)
            phone.height = request.data.get('height', '')
            phone.width = request.data.get('width', '')
            phone.depth = request.data.get('depth', '')
            phone.weight = request.data.get('weight', '')
            phone.storage = request.data.get('storage', '')
            phone.identifier = request.data.get('identifier', '')

            phone.save()

            serializer = PhoneSerializer(phone)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class PhoneDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        phone = Phone.objects.filter(id=id)
        serializer = PhoneSerializer(phone, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        try:
            phone = Phone.objects.get(id=id)

            if request.data.get('brand'):
                try:
                    phone.brand = Brand.objects.get(brand=request.data['brand'])
                except ObjectDoesNotExist:
                    return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)

            if request.data.get('camera'):
                camera = Camera.objects.filter(camera_name=request.data['camera']).first()
                
                if camera:
                    phone.camera = camera
                else:
                    return Response({"error": "Camera not found"}, status=status.HTTP_404_NOT_FOUND)



            if request.data.get('screen_resolution'):
                try:
                    phone.screen_resolution = Screen_resolution.objects.get(resolution=request.data['screen_resolution'])
                except ObjectDoesNotExist:
                    return Response({"error": "Screen resolution not found"}, status=status.HTTP_404_NOT_FOUND)
                
            if request.data.get('color'):
                color = Color.objects.filter(color=request.data['color']).first()
                if color:
                    phone.color = color
                else:
                    return Response({"error": "Color not found"}, status=status.HTTP_404_NOT_FOUND)

            if request.data.get('so'):
                so_data = request.data['so'].split(',')
                if len(so_data) == 2:
                    so_name = so_data[0].strip()
                    firmware = so_data[1].strip()

                    so = So.objects.filter(so=so_name).first()
                    if so:
                        phone.so = so
                        phone.firmware = firmware
                    else:
                        return Response({"error": "S.O. not found"}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({"error": "Invalid format for S.O. and firmware"}, status=status.HTTP_400_BAD_REQUEST)

            phone.model = request.data.get('model', phone.model)
            phone.ram = request.data.get('ram', phone.ram)
            phone.battery = request.data.get('battery', phone.battery)
            phone.price = request.data.get('price', phone.price)
            phone.height = request.data.get('height', phone.height)
            phone.width = request.data.get('width', phone.width)
            phone.depth = request.data.get('depth', phone.depth)
            phone.weight = request.data.get('weight', phone.weight)
            phone.storage = request.data.get('storage', phone.storage)
            phone.identifier = request.data.get('identifier', phone.identifier)

            phone.save()

            serializer = PhoneSerializer(phone)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Phone.DoesNotExist:
            return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PhoneDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        phone = Phone.objects.filter(id=id)
        
        if phone.exists():
            phone.delete()
            return Response({"message": "Teléfono eliminado con éxito"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Teléfono no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
class ColorListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        colors = Color.objects.all()
        color_list = [{"id": color.id, "color": color.color, "hexadecimal": color.color_hex} for color in colors]
        return Response(color_list)

class BrandListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        brands = Brand.objects.all()
        brand_list = [{"id": brand.id, "brand": brand.brand} for brand in brands]
        return Response(brand_list)

class SoListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        so = So.objects.all()
        so_list = [{"id": so.id, "so": so.so, "firmware": so.firmware} for so in so]
        return Response(so_list)

class CameraListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        cameras = Camera.objects.all()
        camera_list = [{"id": camera.id, "camera_name": camera.camera_name} for camera in cameras]
        return Response(camera_list)




