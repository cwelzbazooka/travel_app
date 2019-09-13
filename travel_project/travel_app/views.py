from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from .models import Single_Localisation
from django.contrib.auth.decorators import login_required
from . import plots
from .forms import LocalisationForm



class Map_Travel(TemplateView):
    '''Shows a plot with all localisations user visited'''
    template_name = 'travel_app/plot.html'
    def get_context_data(self, **kwargs):
        context = super(Map_Travel, self).get_context_data(**kwargs)
        context['map_travel'] = plots.get_map_travel()
        return context


def localisation(request, localisation_id):
    '''show a single localisation that user added'''
    localisation = get_object_or_404(Single_Localisation, id=localisation_id)
    if localisation.owner != request.user:
        raise Http404
    context = {'localisation' : localisation} # czy tu powymieniac po kolei?
    return render(request, 'travel_app/localisation.html', context)

def localisations(request):
    '''Shows all localsiations added by user'''
    localisations = Single_Localisation.objects.filter(owner=request.user).order_by('date_added')
    context = {'localisations': localisations}
    return render(request, 'travel_app/localisations.html', context)
 

def add_localisation(request):
    '''adding new localisation'''
    if request.method != 'POST':
        form = LocalisationForm()
        #blank form
    else:
        #POST
        form = LocalisationForm(data=request.POST)
        if form.is_valid():
            new_localisation = form.save(commit=False)
            new_localisation.owner = request.user
            new_localisation.save()
            return redirect('localisations')
    context = {'form':form}
    return render(request, 'travel_app/add_localisation.html', context)
    

# def edit_localisation(request, localisation_id):
#     pass
