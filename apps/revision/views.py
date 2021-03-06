from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView, TemplateView

from apps.revision.models import Revision
from apps.revision.forms import RevisionForm

from apps.registro.models import Registro
# Create your views here.

class RevisionList(ListView):
    model = Revision
    paginate_by = 50
    template_name = "revision/revision_list.html"

    def get_queryset(self):
        queryset = Revision.objects.filter(activo=True).order_by('id')
        return queryset

class Revision2List(ListView):
    model = Revision
    paginate_by = 50
    template_name = "consulta/consulta_list.html"

    def get_queryset(self):
        queryset = Revision.objects.filter(activo=True).order_by('id')
        return queryset


class RevisionCreate(CreateView):
    model = Revision
    form_class = RevisionForm
    template_name = "revision/revision_create.html"
    success_url = reverse_lazy("revision:listar")


class RevisionUpdate(UpdateView):
    model = Revision
    form_class = RevisionForm
    template_name = "revision/revision_create.html"
    success_url = reverse_lazy("revision:listar")


class Revision2Update(UpdateView):
    model = Revision
    form_class = RevisionForm
    template_name = "revision/revision2_create.html"
    success_url = reverse_lazy("revision:listar")


class Revision3Update(UpdateView):
    model = Revision
    form_class = RevisionForm
    template_name = "revision/revision3_create.html"
    success_url = reverse_lazy("revision:listar")

class RevisionDelete(DeleteView):
    model = Revision
    template_name = "revision/revision_delete.html"
    success_url = reverse_lazy("revision:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class BuscarView(TemplateView):

    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']

        idRevision = Revision.objects.filter(id__contains=buscar).order_by('id')
        if idRevision:
            return render(request, 'consulta/buscar.html',
            {'idRevision':idRevision, 'id':True})
        else:
            numOficio = Registro.objects.filter(numeroOficio__contains=buscar).order_by('id')
            
        return render(request, 'consulta/buscar.html',
            {'numOficio':numOficio, 'oficio':True})


class RevisionVisualizar(UpdateView):
    model = Revision
    form_class = RevisionForm
    template_name = "revision/visualizar.html"
    success_url = reverse_lazy("revision:listar")