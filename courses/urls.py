"""codewithgaurav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
#from codewithgaurav.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
#from courses.views import home,coursePage,signup,login OR uses
from courses.views import HomePageView, coursePage , SignupView , LoginView, signout, checkout,verifyPayment,MyCoursesList

urlpatterns = [
    path('',HomePageView.as_view(),name="home" ),
    path('logout',signout,name="logout" ),
    path('my-courses',MyCoursesList.as_view(),name="my-courses"),
    #path('signup',signup,name="signup" ),
    path('signup',SignupView.as_view(),name="signup" ),
    #path('login',login,name="login" ),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>',coursePage,name="coursepage" ),
    path('check-out/<str:slug>',checkout,name="check-out" ),
    path('verify_payment',verifyPayment,name="verify_payment" ),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)