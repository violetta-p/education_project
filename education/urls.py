from django.urls import path
from education.apps import EduModulesConfig
from education.views import ModuleCreateAPIView, ModuleListAPIView, \
    ModuleRetrieveAPIView, ModuleUpdateAPIView, ModuleDestroyAPIView

app_name = EduModulesConfig.name

urlpatterns = [
    path('create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('', ModuleListAPIView.as_view(), name='module_list'),
    path('<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module_get'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module_delete'),
]
