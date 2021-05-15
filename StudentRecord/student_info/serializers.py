from rest_framework import serializers
from .models import StudentInfoModel

class StudentInfoModelSerializers(serializers.ModelSerializer):

    class Meta:  # Overriding StudentInfoModel 1, 2, 3, 4,
        model = StudentInfoModel
        fields = ('st_name', 'collage')
