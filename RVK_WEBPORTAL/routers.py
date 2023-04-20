from rest_framework import routers
from accounts.views import (
    AccountViewSet,
    GroupView
)
from django.urls import path
from posts.views import PostViewSet

#event
from events.views import (
    EventViewSet,
    EventRegisterViewSet,
)

from support.views import SupportViewset
from careers.views import (
    CareerViewset,
    CareerDescModelView
)
from volunteers.views import VolunteerViewset
from contacts.views import ContactViewset
from announcements.views import AnnouncementViewset

#home
from home.views import (
    BannerModelView,
    LatestVideoModelView,
    NewsShelterViewset
)

from password_recover.views import (
    PasswordReset,
    ResetPasswordAPI
)

#news
from news.views import(
    NewsCategoryModelView,
    NewsModelView,
    RecentNewsModelView,
    NewsBanner
)

from about.views import(
    RvkAboutBannerView,
    RvkAboutDescriptionView,
    QuickLinksView
)
from about_prem_rawat.views import(
    PremRawatAboutBannerView,
    PremRawattDescriptionView
)

from media_gallery.views import(
    BannerView,
    GalleryCategoryView,
    MediaView
)

#payment
from events.views import(
    EventRegisterViewSet
)

#initiative
from initiative.views import(
    HumanitarianBottomSectionsView,
    HumanitarianTopSectionView,
    PeaceEducationProgramTopSectionView,
    PeaceEducationProgramSecondSectionView,
    PeaceEducationProgramThiredSectionView,
    PeaceEducationProgramFourthSectionSectionView,
    PeaceEducationProgramAndEducationFirstSectionView,
    PeaceEducationProgramAndEducationSecondSectionView

)






router = routers.DefaultRouter()

#accounts
router.register(r'group',GroupView)



router.register(r'posts',PostViewSet)

#event
router.register(r'events',EventViewSet)
#router.register(r'eventregister',EventRegisterViewSet)


#career
router.register(r'careers',CareerViewset)
router.register(r'careers-desc',CareerDescModelView)


router.register(r'volunteers',VolunteerViewset)
router.register(r'contact',ContactViewset)
router.register(r'announcements',AnnouncementViewset)

#home
router.register(r'home_banner',BannerModelView)
router.register(r'latestvideo',LatestVideoModelView)
router.register(r'newsshelter',NewsShelterViewset)

#router.register(r'donate',DonationView)


#news
router.register(r'news_banner',RecentNewsModelView)
router.register(r'news',NewsModelView)
router.register(r'news_category',NewsCategoryModelView)
router.register(r'recent_news',RecentNewsModelView)



#router.register(r'career_desc',CareerDescModelView)

router.register(r'rvkaboutbanner',RvkAboutBannerView)
router.register(r'rkbaboutdescription',RvkAboutDescriptionView)
router.register(r'quicklinkview',QuickLinksView) 

router.register(r'premrawataboutbanner',PremRawatAboutBannerView)
router.register(r'premrawatdescription',PremRawattDescriptionView)

router.register(r'mediabannerview',BannerView)
router.register(r'gallerycategory',GalleryCategoryView)
router.register(r'mediaview',MediaView)

#initiative
router.register(r'humanitarian-top',HumanitarianTopSectionView)
router.register(r'humanitarian-bottom',HumanitarianBottomSectionsView)
router.register(r'peace-education-program-top',PeaceEducationProgramTopSectionView)
router.register(r'peace-education-program-second',PeaceEducationProgramSecondSectionView)

router.register(r'peace-education-program-thired',PeaceEducationProgramThiredSectionView)
router.register(r'peace-education-program-fourth',PeaceEducationProgramFourthSectionSectionView)
router.register(r'peace-education-program-and-education-first',PeaceEducationProgramAndEducationFirstSectionView)
router.register(r'peace-education-program-and-education-second',PeaceEducationProgramAndEducationSecondSectionView)






urlpatterns = [
    #path('event_register/', EventRegisterViewSet.as_view(), name="event_register"),
    # path('reset-password/', PasswordReset.as_view(), name="reset-password/"),
    # path('reset-password/<str:encoded_pk>/<str:token>/',ResetPasswordAPI.as_view()),
    
]+ router.urls