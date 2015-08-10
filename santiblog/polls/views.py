from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from polls.models import Post, Coment, Categoria
from django.core.mail import send_mail

def verhome(request):
    context = RequestContext(request)
    categorias = Categoria.objects.all()
    posts = Post.objects.all()
    coments = Coment.objects.all()
    return render_to_response('index.html',
                              {'posts':posts, 'coments':coments, 'categorias':categorias},
                              context)

def vercv(request):
    context = RequestContext(request)
    return render_to_response('Curriculum.html',
                              context)
# Create your views here.

def verbtnmg(request):
    context = RequestContext(request)
    return render_to_response('Boton.html',
                             context)
# Create your views here.

def vercal(request):
    context = RequestContext(request)
    return render_to_response('Calculadora.html',
                              context)
# Create your views here.

def vercon(request):
    context = RequestContext(request)
    return render_to_response('Contacto.html',
                              context)
# Create your views here.

def verconv(request):
    context = RequestContext(request)
    return render_to_response('Conversor.html',
                              context)
# Create your views here.

def vercro(request):
    context = RequestContext(request)
    return render_to_response('Cronometro.html',
                              context)
# Create your views here.

def verimagen(request):
    context = RequestContext(request)
    return render_to_response('Barra.html',context)

# Create your views here.
def vernoticias(request):
    context = RequestContext(request)
    noticias = Post.objects.all()
    return render_to_response('Noticias.html',
                              {'posts':noticias},
                              context)

def ver_post(request, id_post):
    context = RequestContext(request)
    post = Post.objects.get(id=id_post)
    coments = Coment.objects.filter(post=post, published = True)
    return render_to_response('posts.html', 
                              {'post':post, 'coments':coments},
                              context)
def save_message(request):
    context = RequestContext(request)
    coment_txt = None
    if request.method == 'POST':
        mi_post =               Post.objects.get(id=request.POST['id'])
        print(mi_post)
        titulo_txt= request.POST['titulo_txt']
        coment_txt= request.POST['coment_txt']        
        msje = Coment()
        msje.titulo_txt = titulo_txt
        msje.coment_txt = coment_txt
        msje.post = mi_post
        msje.save()
        coments = Coment.objects.filter(post=mi_post, published = True)

    return render_to_response('mensajes.html', 
                              {'coments':coments},
                              context)
def contact(request):
    context  = RequestContext(request)
    
    if request.method=="POST":
        nombre = request.POST["nombre"]
        emailRemit = request.POST["email"]
        mensaje = request.POST["mensaje"]
        send_mail(str(nombre), str(mensaje), emailRemit,['mateofede98@gmail.com'], fail_silently=False)
    return render_to_response("contact.html",
                             context)

def categoria(request, categoria):
    context = RequestContext(request)
    categoria = Categoria.objects.get(id=categoria)
    post = Post.objects.filter(categoria=categoria)
    return render_to_response('categoria.html', 
                              {'post':post, 'categoria':categoria},
                              context)
