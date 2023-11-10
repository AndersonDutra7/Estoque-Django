from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('search-product/', views.search_product, name='search-product'),
    path("add-product/", views.add_product, name="add-product"),
    path("delete-product/<int:id>/", views.delete_product, name="delete-product"),
    path("sell-product/<int:id>/", views.sell_product, name="sell-product"),
    path("product-detail/<int:id>/", views.product_detail, name="product-detail"),
]

# Adicione as seguintes linhas para lidar com arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
