from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login,name='login'),
    url(r'^signup/$', views.signup,name='signup'),
    url(r'^loginReq/',views.loginReq, name = 'loginReq'),
    url(r'^gestionproductos/$', views.gestionproductos,name='gestionproductos'),
    url(r'^vendedorprofilepage/$', views.vendedorprofilepage,name='vendedorprofilepage'),
    url(r'^formView/', views.formView, name='formView'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^loggedin/', views.loggedin, name='loggedin'),
    url(r'^productoReq/', views.productoReq, name='productoReq'),
    url(r'^vistaVendedorPorAlumno/', views.vistaVendedorPorAlumno, name='vistaVendedorPorAlumno'),
    url(r'^inicioAlumno/', views.inicioAlumno, name='inicioAlumno'),
    url(r'^borrarUsuario/', views.borrarUsuario, name='borrarUsuario'),
    url(r'^borrarProducto/', views.borrarProducto, name='borrarProducto'),
    url(r'^editarProducto/', views.editarProducto, name='editarProducto'),
    url(r'^cambiarFavorito/', views.cambiarFavorito, name='cambiarFavorito'),
    url(r'^vistaVendedorPorAlumnoSinLogin/', views.vistaVendedorPorAlumnoSinLogin, name='vistaVendedorPorAlumnoSinLogin'),
    url(r'^editarPerfilAlumno/', views.editarPerfilAlumno,name='editarPerfilAlumno'),
    url(r'^procesarPerfilAlumno/', views.procesarPerfilAlumno,name='procesarPerfilAlumno'),
    url(r'^editarUsuario/', views.editarUsuario, name='editarUsuario'),
    url(r'^agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    url(r'^signupAdmin/$', views.signupAdmin,name='signupAdmin'),
    url(r'^registerAdmin/$', views.registerAdmin,name='registerAdmin'),
    url(r'^getStock/$', views.getStock,name='getStock'),
    url(r'^verificarEmail/$', views.verificarEmail,name='verificarEmail'),
]
