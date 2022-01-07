from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import (CompanyDetailView, CompanyPeopleView, CompanySettingView, 
                    CompanyTaskDetailView, CompanyTaskView)


urlpatterns = [
    path('detail/', CompanyDetailView.as_view(), name='detail'),
    path('people/', CompanyPeopleView.as_view(), name='people'),
    path('settings/', CompanySettingView.as_view(), name='settings'),
    path('task-detail/', CompanyTaskDetailView.as_view(), name='task-detail'),
    path('task/', CompanyTaskView.as_view(), name='task'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)