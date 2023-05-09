from django.urls import path
from . import views
app_name = 'engine'


urlpatterns = [
    path('login', views.loginView, name='loginurls'),
    path('logout', views.logoutView, name='logoutUrl'),
    path('', views.homeView, name='homeURL'),
    path('teachers', views.teachersView, name='teachersURL'),
    path('students', views.studentsView, name='studentsURL'),
    path('addstudent', views.addstudentView, name='addstudentURL'),
    path('editstudent', views.editstudentView, name='editstudentURL'),
    path('aboutstudent', views.aboutstudentView, name='aboutstudentURL'),
    path('calendar', views.calendarView, name='calendarURL'),
    path('setting', views.settingView, name='settingURL'),
    path('changep', views.changepView, name='changepURL'),
    path('blog', views.blogView, name='blogURL'),
    path('blogview', views.blogviewView, name='blogviewURL'),
    path('addblog', views.addblogView, name='addblogURL'),
    path('editblog', views.editblogView, name='editblogURL'),
    path('chat', views.chatView, name='chatURL'),
    path('myprofile', views.myprofileView, name='myprofileURL'),
    path('editpro', views.editproView, name='editproURL'),
    path('ssetting', views.ssettingView, name='ssettingURL'),
    #path('/home', views.homeView, name='homeURL'),
]
