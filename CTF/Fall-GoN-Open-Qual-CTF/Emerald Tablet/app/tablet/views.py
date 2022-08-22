from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Inscription, Content
from .forms import ListForm, ViewForm, InscriptionForm, ContentForm


class ListView(TemplateView):
    template_name = 'list.html'

    def get(self, request):
        form = ListForm(request.GET)
        if not form.is_valid():
            return redirect('/list/')
        sort_key = form.cleaned_data['sort']
        
        sort_rev = False
        if sort_key.startswith('-'):
            sort_key = sort_key[1:]
            sort_rev = True
        
        inscriptions = Inscription.objects.all().values()

        return self.render_to_response({
            'sort_key': sort_key,
            'sort_rev': sort_rev,
            'inscriptions': inscriptions,
        })


class ViewView(TemplateView):
    template_name = 'view.html'

    def get(self, request):
        form = ViewForm(request.GET)
        if not form.is_valid():
            return self.render_to_response({
                'form': ViewForm(),
                'alertText': None,
            })
        _id = form.cleaned_data['id']
        key = form.cleaned_data['key']

        try:
            inscription = Inscription.objects.get(id=_id)
        except Inscription.DoesNotExist:
            return self.render_to_response({
                'form': form,
                'alertText': f'Inscription #{_id} does not exist.',
            })
        
        if inscription.key != key:
            return self.render_to_response({
                'form': form,
                'alertText': f'Key {key} is invalid for inscription #{_id}.',
            })
        
        return self.render_to_response({
            'form': None,
            'inscription': inscription,
        })


class UploadView(TemplateView):
    template_name = 'upload.html'

    def get(self, request):
        return self.render_to_response({
            'form_inscription': InscriptionForm(),
            'form_content': ContentForm(),
        })
    
    def post(self, request):
        form_inscription = InscriptionForm(request.POST)
        form_content = ContentForm(request.POST)
        if not (form_inscription.is_valid() and form_content.is_valid()):
            return self.render_to_response({
                'form_inscription': form_inscription,
                'form_content': form_content,
            })
        
        inscription = form_inscription.save()
        content = form_content.save(commit=False)
        content.inscription = inscription
        content.save()

        return redirect(f'/list/')
