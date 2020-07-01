from rest_framework import serializers
from .models import Bank,Branch


class Branchserialzer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"