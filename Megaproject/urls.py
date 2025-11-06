from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from tweet import views as tweet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', tweet_views.register, name='register'),


    path('', RedirectView.as_view(url='/tweet/', permanent=False)),    #isse automatcially tweet pr jump kr jayega bro
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



