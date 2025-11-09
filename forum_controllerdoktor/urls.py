"""
URL configuration for forum_controllerdoktor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
#log in logout 
from django.contrib.auth import views as auth_views 

# sitemaps
from django.contrib.sitemaps.views import sitemap
from sitemaps import ForumSitemap, TopicSitemap, RecentPostsSitemap
import sitemaps

from Forum_home.views import forum_home 
from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', forum_home, name='forum_home'),
    # machina forum urls
    path('forum/', include(machina_urls)),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # robots.txt
    path('robots.txt', include('robots.urls')),
    # Sitemaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]



# Sitemaps configuration
sitemaps = {
    'forums': ForumSitemap,
    'topics': TopicSitemap,
    'posts': RecentPostsSitemap,
}
