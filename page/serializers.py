from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = '__all__'

class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    fanlar = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()


    # subject_name = serializers.SerializerMethodField()
    # teacher_name = serializers.SerializerMethodField()
    # room_no = serializers.SerializerMethodField()
    # table = serializers.SerializerMethodField()
    # fanlar = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = '__all__'
        # fields = ['id', 'group_name','fanlar']

    def get_group_name(self, obj):
        if obj.group_name:
            return obj.group_name.name
        return 0

    def get_fanlar(self, obj):
        fanlar = Fanlar.objects.filter(table=obj).all()
        if fanlar:
            return FanlarSerializer(fanlar, many=True, context={'request': self.context['request']}).data
        return None

    # def get_subject_name(self, obj):
    #     if obj.subject_name:
    #         return obj.subject_name.name
    #     return 0

    # def get_teacher_name(self, obj):
    #     if obj.teacher_name:
    #         return obj.teacher_name.name
    #     return 0

    # def get_room_no(self, obj):
    #     if obj.room_no:
    #         return obj.room_no.name
    #     return 0

    # def get_fanlar(self, obj):
    #     fanlar = Fanlar.objects.filter(table=obj).all()
    #     return FanlarSerializer(fanlar, many=True, context={'request': self.context['request']}).data


class Fanlarser(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = "__all__"

class FanlarSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    room_no = serializers.SerializerMethodField()
    # fanlar = serializers.SerializerMethodField()

    class Meta:
        model = Fanlar
        fields = "__all__"

    def get_subject_name(self, obj):
        if obj.subject_name:
            return obj.subject_name.name
        return 0

    def get_teacher_name(self, obj):
        if obj.teacher_name:
            return obj.teacher_name.name
        return 0

    def get_room_no(self, obj):
        if obj.room_no:
            return obj.room_no.name
        return 0

    # def get_fanlar(self, obj):
    #     fanlar = Fanlar.objects.filter(table=obj).all()
    #     return FanlarSerializer(fanlar, many=True, context={'request': self.context['request']}).data
