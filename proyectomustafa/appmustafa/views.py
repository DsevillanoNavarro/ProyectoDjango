from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Animal, Noticia, Comentario
from .forms import animales_form, noticias_form, comentarios_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

def principal(request):
    return render(request, 'appmustafa/principal.html')

class CrearRegistro(CreateView):
    form_class = UserCreationForm
    template_name = 'appmustafa/registro.html'
    success_url = reverse_lazy('login')
    
class Animales(ListView):
    model=Animal
    template_name='appmustafa/animales.html'
    context_object_name = 'animales'
    
    
    def get_queryset(self):
        orden = self.request.GET.get('orden', 'desc')  
        if orden == 'asc':
            return Animal.objects.all().order_by('edad')  
        return Animal.objects.all().order_by('-edad')  
    
class CrearAnimales(LoginRequiredMixin, CreateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/crearAnimales.html'
    success_url = reverse_lazy('listarAnimales')
class EditarAnimales(UpdateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/editarAnimales.html'
    success_url = reverse_lazy('listarAnimales')

class BorrarAnimales(DeleteView):
    model=Animal
    template_name = 'appmustafa/borrarAnimales.html'
    success_url = reverse_lazy('listarAnimales')
    
class ListarAnimales(ListView):
    model=Animal
    template_name='appmustafa/listarAnimalesAdmin.html'
    context_object_name = 'animales'
    
class DetallesAnimales(DetailView):
    model = Animal
    template_name = 'appmustafa/detalleAnimal.html' 
    context_object_name = 'animal'
    
class CrearNoticias(CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('noticias')

class UserMenuView(TemplateView):
    template_name = 'appmustafa/usuario.html'
    
class CrearNoticias(LoginRequiredMixin, CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('listarNoticias')
    
class ListarNoticias(ListView):
    model=Noticia
    template_name='appmustafa/listarNoticiasAdmin.html'
    context_object_name = 'noticias'
    
class EditarNoticias(UpdateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/editarNoticias.html'
    success_url = reverse_lazy('listarNoticias')
class BorrarNoticias(DeleteView):
    model=Noticia
    template_name = 'appmustafa/borrarNoticias.html'
    success_url = reverse_lazy('listarNoticias')

class Noticias(ListView):
    model=Noticia
    template_name='appmustafa/noticias.html'
    context_object_name = 'noticias'

class DetallesNoticias(DetailView):
    model = Noticia
    template_name = 'appmustafa/detalleNoticia.html' 
    context_object_name = 'noticia'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(noticia=self.object)
        context['form'] = comentarios_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 
        form = comentarios_form(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = self.object
            if request.user.is_authenticated:
                comentario.usuario = request.user
            else:
                return redirect('login')
            
            comentario.save()
            return redirect(reverse('detalleNoticias', kwargs={'pk': self.object.pk}))
        return self.render_to_response(self.get_context_data(form=form))

class ListarComentarios(ListView):
    model=Comentario
    template_name='appmustafa/listarComentarios.html'
    context_object_name = 'comentarios'

class EditarComentarios(UpdateView):
    model=Comentario
    form_class = comentarios_form
    template_name = 'appmustafa/editarComentarios.html'
    success_url = reverse_lazy('editarComentarios')
class BorrarComentarios(DeleteView):
    model=Comentario
    template_name = 'appmustafa/borrarComentarios.html'
    success_url = reverse_lazy('listarComentarios')
