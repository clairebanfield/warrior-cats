from django.shortcuts import render
from graphviz import Digraph

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError

from .models import Clan, Cat, CatForm
from .forms import ClanForm

def index(request):
    template = loader.get_template('create_warrior/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def addcat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
        #Process the Data
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            clan = form.cleaned_data['clan']
            position = form.cleaned_data['position']
            newcat = Cat(name=name,
                         age=age,
                         clan=clan,
                         position=position)
            newcat.save()
            template = loader.get_template('create_warrior/save_success.html')
            target = 'Cat'
            context = {'target': target,}
            return HttpResponse (template.render(context,request))
    else:
        form = CatForm()
        template = loader.get_template('create_warrior/addcat.html')
        context = {'form': form,}
        return HttpResponse(template.render(context, request))

def editcat(request, name):
    cat = []
    cat = Cat.objects.filter(name=name)[0]        
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)                    
        form.save()
        template = loader.get_template('create_warrior/save_success.html')
        target = 'Cat'
        context = {'target': target,}
        return HttpResponse (template.render(context,request))
    else:
        form = CatForm(instance=cat)                    
        template = loader.get_template('create_warrior/editcat.html')
        context = {'form': form, 'cat': cat}
        return HttpResponse(template.render(context, request))    

def deletecat(request, name):
    cat = []
    cat = Cat.objects.filter(name=name)[0]
    cat.delete()
    template = loader.get_template('create_warrior/delete_success.html')
    target = 'Cat'
    context = {'target': target,}    
    return HttpResponse(template.render(context, request))

def deleteclan(request, name):
	clan = []
	clan = Clan.objects.filter(name=name)[0]
	for x in clan.cat_set.all():
		x.delete()
	clan.delete()
	template = loader.get_template('create_warrior/delete_success.html')
	target = 'Clan'
	context = {'target': target,}    
	return HttpResponse(template.render(context, request))
	
def addclan(request):
    if request.method == 'POST':
        form = ClanForm(request.POST)
        if form.is_valid():
        #Process the Data
            name = form.cleaned_data['name']
            habitat = form.cleaned_data['habitat']
            newclan = Clan(name=name, habitat=habitat)
            newclan.save()
            template = loader.get_template('create_warrior/save_success.html')
            target = 'Clan'
            context = {'target': target,}
            return HttpResponse (template.render(context,request))
    else:
        form = ClanForm()
        template = loader.get_template('create_warrior/addclan.html')
        context = {'form': form,}
        return HttpResponse(template.render(context, request))

def catlist(request):
    clan_list = []
    clan_list = Clan.objects.all()
    template = loader.get_template('create_warrior/list.html')
    context = {'clan_list': clan_list,}
    return HttpResponse(template.render(context, request))



def catdetails(request, name):
    cat = []
    cat = Cat.objects.filter(name=name)[0]
    template = loader.get_template('create_warrior/catdetails.html')
    context = {'cat': cat,}
    return HttpResponse(template.render(context, request))

def clandetails(request, name):
    clan = []
    clan = Clan.objects.filter(name=name)[0]
    try:
        leader = clan.cat_set.filter(position='LD')[0]
    except IndexError:
        template = loader.get_template('create_warrior/leader_error.html')
        context = {'clan': clan,}
        return HttpResponse(template.render(context, request))
    try:
        deputy = clan.cat_set.filter(position='DY')[0]
    except IndexError:
        template = loader.get_template('create_warrior/deputy_error.html')
        context = {'clan': clan,}
        return HttpResponse(template.render(context, request))
    
    warriors = clan.cat_set.filter(position='WR')

    dot = Digraph(name='clan-graph',
                  node_attr={'fillcolor': 'white', 'style' : 'filled'},
                  edge_attr={'fillcolor': 'white', 'color' : 'white'}
                  )
    dot.format = 'png'
    dot.graph_attr['bgcolor'] = 'transparent'
    dot.node('L', leader.name)
    dot.node('D', deputy.name)
    for x in warriors:
        dot.node('W' + str(x.id), x.name)
    
    
    dot.edge('L', 'D')
    for x in warriors:
        dot.edge('D', 'W' + str(x.id))

    graph = dot.render('create_warrior/static/create_warrior/images/graph', view=False)
    graph = '../images/' + graph
    template = loader.get_template('create_warrior/clandetails.html')
    context = {'clan': clan, 'graph': graph,}
    return HttpResponse(template.render(context, request))
    
    
