# urls.py

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from food.views import (
    receipes,
    update_receipe,
    delete_receipe,
    recipe_details,
    add_receipe,
    login_page,
    registration_page,
    user_profile,
)
from food.api_views import ReceipeListCreateView, ReceipeDetailView
from vege import settings

urlpatterns = [
    # Regular Django Views
    path('', receipes, name='receipes'),
    path('login/', login_page, name='login'),
    path('register/', registration_page, name='registration'),
    # Add other paths for your views...
   path('admin/', admin.site.urls),
    path('user_profile/', user_profile, name='user_profile'),
    path('update-receipe/<int:id>/', update_receipe, name='update_receipe'),
    path('delete-receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('recipe/<int:recipe_id>/', recipe_details, name='recipe_details'),
    path('add_receipe.html', add_receipe, name='add_receipe'),

    # Django REST Framework Views
    path('api/receipes/', ReceipeListCreateView.as_view(), name='api-receipes'),
    path('api/receipes/<int:pk>/', ReceipeDetailView.as_view(), name='api-receipe-detail'),

    # Add the following line to serve media files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('admin/', admin.site.urls),
]
