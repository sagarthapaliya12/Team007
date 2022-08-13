from django.urls import path

from tumordetection.views import ImageView

urlpatterns = [
    path('set/', ImageView.as_view(), name='setImage'),

]