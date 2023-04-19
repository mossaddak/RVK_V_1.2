from django.shortcuts import render

from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)
from RVK_WEBPORTAL.permissions import(
    IsContentEditor
)
from rest_framework.views import (
    APIView
)

from .serializer import(
    HumanitarianTopSectionSerializer,
    HumanitarianBottomSectionsSerializer,
    PeaceEducationProgramTopSectionSerializer,
    PeaceEducationProgramSecondSectionSerializer,
    PeaceEducationProgramThiredSectionSerializer,
    PeaceEducationProgramFourthSectionSerializer,
    PeaceEducationProgramAndEducationFirstSectionSerializer,
    PeaceEducationProgramAndEducationSecondSectionSerializer
   
)
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


#Humanitarian
class HumanitarianTopSectionView(ModelViewSet):
    
    serializer_class = HumanitarianTopSectionSerializer
    queryset = HumanitarianTopSection.objects.all()
    permission_classes = [IsContentEditor]

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class HumanitarianBottomSectionsView(ModelViewSet):
    serializer_class = HumanitarianBottomSectionsSerializer
    queryset = HumanitarianBottomSections.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


#peace education
class PeaceEducationProgramTopSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramTopSectionSerializer
    queryset = PeaceEducationProgramTopSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class PeaceEducationProgramSecondSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramSecondSectionSerializer
    queryset = PeaceEducationProgramSecondSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class PeaceEducationProgramThiredSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramThiredSectionSerializer
    queryset = PeaceEducationProgramThiredSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class PeaceEducationProgramFourthSectionSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramFourthSectionSerializer
    queryset = PeaceEducationProgramFourthSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

#Peace Education & Knowledge
class PeaceEducationProgramAndEducationFirstSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramAndEducationFirstSectionSerializer
    queryset = PeaceEducationProgramAndEducationFirstSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class PeaceEducationProgramAndEducationSecondSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramAndEducationSecondSectionSerializer
    queryset = PeaceEducationProgramAndEducationSecondSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

# class AllInitiative(APIView):
#     humanitarian_top = HumanitarianTopSection.objects.all()
#     humanitarian_bottom = HumanitarianBottomSections.objects.all()
#     all_q = humanitarian_top | humanitarian_bottom


