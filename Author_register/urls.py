
from django.urls import path
from .views import author_list
from .views import book_list
from .views import authorCreate
from .views import bookCreate
from .views import authorUpdate
from .views import bookUpdate
from .views import authorDelete
from .views import bookDelete

urlpatterns = [
    path('author/', author_list),
    path('book/', book_list),
    path('author_create/', authorCreate),
    path('book_create/', bookCreate),
    path('author_update/<int:pk>/', authorUpdate),
    path('book_update/<int:pk>/', bookUpdate),
    path('author_delete/<int:pk>/', authorDelete),
     path('book_delete/<int:pk>/', bookDelete),

    

   
]