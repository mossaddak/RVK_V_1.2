from django.contrib import admin
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

# Register your models here.
admin.site.register(HumanitarianTopSection)
admin.site.register(HumanitarianBottomSections)
admin.site.register(PeaceEducationProgramTopSection)
admin.site.register(PeaceEducationProgramSecondSection)
admin.site.register(PeaceEducationProgramThiredSection)
admin.site.register(PeaceEducationProgramFourthSection)
admin.site.register(PeaceEducationProgramAndEducationFirstSection)
admin.site.register(PeaceEducationProgramAndEducationSecondSection)
