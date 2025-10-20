# Cada vista está protegida con 'login_required' para asegurar que solo usuarios
# autenticados puedan acceder a las operaciones de creación/edición/eliminación
# de solicitudes.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import Solicitud, Categoria
from .forms import SolicitudForm
from django.db.models import Q


# Vista principal que muestra las solicitudes relevantes para el usuario.
@login_required
def home(request):

    # Seleccionamos solicitudes creadas por el usuario actual o creadas por superuser
    solicitudes = Solicitud.objects.filter(
        Q(creador=request.user) | Q(creador__is_superuser=True)
    ).select_related('categoria', 'creador')

    # Aplicar filtro por estado si se proporciona en la querystring
    estado_filtro = request.GET.get('estado')
    if estado_filtro:
        solicitudes = solicitudes.filter(estado=estado_filtro)
        request.session['filtros'] = {'estado': estado_filtro}

    return render(request, 'home.html', {'solicitudes': solicitudes})


# Cierra la sesión del usuario y redirige al login.
@login_required
def logout_view(request):

    logout(request)
    return redirect('login')


# Crear una nueva 'Solicitud'
@login_required
def crear_solicitud(request):

    # En solicitudes POST: valida el formulario, asigna `creador` como el
    #  usuario autenticado y guarda la instancia.
    # En GET: renderiza el formulario vacío para que el usuario lo rellene.

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            # Creamos la instancia sin guardarla para asignar el creador
            solicitud = form.save(commit=False)
            solicitud.creador = request.user
            solicitud.save()
            # Guardar relaciones M2M si el formulario las tuviera
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            messages.success(request, '¡Solicitud creada exitosamente!')
            return redirect('home')

        # Si el formulario no es válido, volvemos a renderizarlo con errores
        return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Nueva Solicitud'})
    else:
        form = SolicitudForm()

    return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Nueva Solicitud'})


# Editar una 'Solicitud' existente identificada por 'pk'
@login_required
def editar_solicitud(request, pk):

   
    # Permisos: solo el creador de la solicitud o un superusuario pueden editarla.
    solicitud = get_object_or_404(Solicitud, pk=pk)

    # Comprobación simple de permisos: creador o superuser
    if not (request.user.is_superuser or solicitud.creador == request.user):
        messages.error(request, 'No tienes permiso para editar esta solicitud.')
        return redirect('home')

    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Solicitud actualizada!')
            return redirect('home')
    else:
        form = SolicitudForm(instance=solicitud)

    return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Editar Solicitud'})


# Eliminar una 'Solicitud' tras confirmar la acción.
@login_required
def eliminar_solicitud(request, pk):
    # Permisos: solo el creador o un superusuario pueden eliminar.
    # En GET se muestra la confirmación; en POST se elimina y se notifica.

    solicitud = get_object_or_404(Solicitud, pk=pk)

    if not (request.user.is_superuser or solicitud.creador == request.user):
        messages.error(request, 'No tienes permiso para eliminar esta solicitud.')
        return redirect('home')

    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect('home')

    return render(request, 'confirm_delete.html', {'solicitud': solicitud})