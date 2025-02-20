from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .mixins import StaffRequiredMixin
from .models import Animal, Noticia, Comentario, Adopcion
from .forms import animales_form, noticias_form, comentarios_form, adopciones_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q

def sobreNosotros(request):
    return render(request, 'appmustafa/sobrenosotros.html')
def contacto(request):
    return render(request, 'appmustafa/contacto.html')
def principal(request):
    # Obtener los 4 últimos animales registrados (por el ID, que se incrementa automáticamente)
    animales = Animal.objects.all().order_by('-id')[:4]

    # Obtener las 3 últimas noticias (por el ID, que se incrementa automáticamente)
    noticias = Noticia.objects.all().order_by('-id')[:3]

    return render(request, 'appmustafa/principal.html', {
        'animales': animales,
        'noticias': noticias
    })

class CrearRegistro(CreateView):
    form_class = UserCreationForm
    template_name = 'appmustafa/registro.html'
    success_url = reverse_lazy('login')
    
class Animales(ListView):
    model=Animal
    template_name='appmustafa/animales.html'
    context_object_name = 'animales'
    paginate_by = 6
    def get_queryset(self):
        orden = self.request.GET.get('orden', 'desc')  
        if orden == 'asc':
            return Animal.objects.all().order_by('edad')  
        return Animal.objects.all().order_by('-edad')  
    
class CrearAnimales(LoginRequiredMixin, StaffRequiredMixin , CreateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/crearAnimales.html'
    success_url = reverse_lazy('listarAnimales')
    
    def form_valid(self, form):
        messages.success(self.request, 'Animal creado correctamente')
        return super().form_valid(form)
    
class EditarAnimales(LoginRequiredMixin, StaffRequiredMixin ,UpdateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/editarAnimales.html'
    success_url = reverse_lazy('listarAnimales')

    def form_valid(self, form):
        messages.success(self.request, 'Animal editado correctamente')
        return super().form_valid(form)

class BorrarAnimales(LoginRequiredMixin, StaffRequiredMixin ,DeleteView):
    model=Animal
    template_name = 'appmustafa/borrarAnimales.html'
    success_url = reverse_lazy('listarAnimales')

    def form_valid(self, form):
        messages.success(self.request, 'Animal eliminado correctamente')
        return super().form_valid(form)
    
class ListarAnimales(LoginRequiredMixin, StaffRequiredMixin ,ListView):
    model=Animal
    template_name='appmustafa/listarAnimalesAdmin.html'
    context_object_name = 'animales'
    
class DetallesAnimales(DetailView):
    model = Animal
    template_name = 'appmustafa/detalleAnimal.html' 
    context_object_name = 'animal'
    
class CrearNoticias(LoginRequiredMixin, StaffRequiredMixin ,CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('noticias')

    def form_valid(self, form):
        messages.success(self.request, 'Noticia creada correctamente')
        return super().form_valid(form)

class UserMenuView(TemplateView):
    template_name = 'appmustafa/usuario.html'
    
class ListarNoticias(LoginRequiredMixin, StaffRequiredMixin ,ListView):
    model=Noticia
    template_name='appmustafa/listarNoticiasAdmin.html'
    context_object_name = 'noticias'

class EditarNoticias(LoginRequiredMixin, StaffRequiredMixin ,UpdateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/editarNoticias.html'
    success_url = reverse_lazy('listarNoticias')

    def form_valid(self, form):
        messages.success(self.request, 'Noticia editada correctamente')
        return super().form_valid(form)

class BorrarNoticias(LoginRequiredMixin, StaffRequiredMixin ,DeleteView):
    model=Noticia
    template_name = 'appmustafa/borrarNoticias.html'
    success_url = reverse_lazy('listarNoticias')

    def form_valid(self, form):
        messages.success(self.request, 'Noticia eliminada correctamente')
        return super().form_valid(form)

class Noticias(ListView):
    model=Noticia
    template_name='appmustafa/noticias.html'
    context_object_name = 'noticias'
    paginate_by = 3
    
    def get_queryset(self):
        query = self.request.GET.get('buscaNoticia', '')  
        queryset = Noticia.objects.all().order_by('-fecha_publicacion')  
        if query:
            queryset = queryset.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buscaNoticia"] = self.request.GET.get('buscaNoticia', '')  
        return context

class DetallesNoticias(DetailView):
    model = Noticia
    template_name = 'appmustafa/detalleNoticia.html' 
    context_object_name = 'noticia'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(noticia=self.object).order_by('-fecha_hora')
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
            messages.success(self.request, 'Comentario agregado correctamente')
            return redirect(reverse('detalleNoticias', kwargs={'pk': self.object.pk}))
        return self.render_to_response(self.get_context_data(form=form))

class ListarComentarios(LoginRequiredMixin, StaffRequiredMixin ,ListView):
    model=Comentario
    template_name='appmustafa/listarComentarios.html'
    context_object_name = 'comentarios'

class EditarComentarios(LoginRequiredMixin, StaffRequiredMixin ,UpdateView):
    model=Comentario
    form_class = comentarios_form
    template_name = 'appmustafa/editarComentarios.html'
    success_url = reverse_lazy('editarComentarios')

    def form_valid(self, form):
        messages.success(self.request, 'Comentario editado correctamente')
        return super().form_valid(form)

class BorrarComentarios(LoginRequiredMixin, StaffRequiredMixin ,DeleteView):
    model=Comentario
    template_name = 'appmustafa/borrarComentarios.html'
    success_url = reverse_lazy('listarComentarios')

    def form_valid(self, form):
        messages.success(self.request, 'Comentario eliminado correctamente')
        return super().form_valid(form)

class CrearAdopciones(LoginRequiredMixin, CreateView):
    model = Adopcion
    fields = ['contenido']
    template_name = 'appmustafa/crearAdopciones.html' 
    success_url = reverse_lazy('animales')  

    def form_valid(self, form):
        usuario = self.request.user
        animal = get_object_or_404(Animal, id=self.kwargs.get('pk'))

        # Verificar si el usuario ya ha adoptado este animal
        if Adopcion.objects.filter(usuario=usuario, animal=animal).exists():
            messages.error(self.request, 'Ya has adoptado este animal anteriormente.')
            return redirect(self.success_url)  # Redirige sin crear la adopción

        form.instance.usuario = usuario
        form.instance.animal = animal
        messages.success(self.request, 'Adopción realizada correctamente.')
        return super().form_valid(form)


class ListarAdopciones(LoginRequiredMixin, StaffRequiredMixin ,ListView):
    model=Adopcion
    template_name='appmustafa/listarAdopcionesAdmin.html'
    context_object_name = 'adopciones'

class DetalleAdopciones(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Adopcion
    fields = '__all__'
    template_name = 'appmustafa/detalleAdopciones.html'
    context_object_name = 'adopcion'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Aceptar la adopción
        self.object.aceptada = True
        self.object.save()

        # Eliminar todas las adopciones no aceptadas para el mismo animal
        animal = self.object.animal  # Ajusta 'animal' a la relación de tu modelo

        # Elimina todas las adopciones no aceptadas para este animal, excepto la actual
        Adopcion.objects.filter(animal=animal).exclude(id=self.object.id).delete()

        messages.success(self.request, 'Adopción aceptada correctamente y otras adopciones relacionadas han sido eliminadas.')
        
        return redirect('detalleAdopciones', pk=self.object.id)
    
class BorrarAdopciones(LoginRequiredMixin, StaffRequiredMixin ,DeleteView):
    model=Adopcion
    template_name = 'appmustafa/borrarAdopciones.html'
    success_url = reverse_lazy('listarComentarios')

    def form_valid(self, form):
        messages.success(self.request, 'Adopción eliminada correctamente')
        return super().form_valid(form)
