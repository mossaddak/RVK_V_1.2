from rest_framework import serializers

from .models import(
    HumanitarianTopSection,
    HumanitarianBottomSections,
    PeaceEducationProgramTopSection,
    PeaceEducationProgramSecondSection,
    PeaceEducationProgramThiredSection,
    PeaceEducationProgramFourthSection,
    PeaceEducationProgramAndEducationFirstSection,
    PeaceEducationProgramAndEducationSecondSection
)

class HumanitarianTopSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HumanitarianTopSection
        fields = "__all__"

class HumanitarianBottomSectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HumanitarianBottomSections
        fields = "__all__"


class PeaceEducationProgramTopSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramTopSection
        fields = "__all__"

class PeaceEducationProgramSecondSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramSecondSection
        fields = "__all__"

class PeaceEducationProgramThiredSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramThiredSection
        fields = "__all__"

class PeaceEducationProgramFourthSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramFourthSection
        fields = "__all__"

class PeaceEducationProgramAndEducationFirstSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramAndEducationFirstSection
        fields = "__all__"

class PeaceEducationProgramAndEducationSecondSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramAndEducationSecondSection
        fields = "__all__"



