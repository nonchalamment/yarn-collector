from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('yarns/', views.yarn_index, name='yarn-index'),
  path('yarns/<int:yarn_id>/', views.yarn_detail, name='yarn-detail'),
  path('yarns/create/', views.YarnCreate.as_view(), name='yarn-create'),
  path('yarns/<int:pk>/update/', views.YarnUpdate.as_view(), name='yarn-update'),
  path('yarns/<int:pk>/delete/', views.YarnDelete.as_view(), name='yarn-delete'),
  path('yarns/<int:yarn_id>/add-dusting/', views.add_dusting, name='add-dusting'),
  path('yarns/<int:cat_id>/assoc-project/<int:project_id>/', views.assoc_project, name='assoc-project'),
  path('accounts/signup/', views.signup, name='signup'),
  path('projects/create', views.ProjectCreate.as_view(), name='project-create'),
  path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
  path('projects/', views.ProjectList.as_view(), name='project-index'),
  path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
]