from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import choice
import markdown2


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    
    else:
        entry = util.get_entry(title)
        entry = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "title": title
        })
    

def search(request):
    query = request.GET.get('q')


    for entry in util.list_entries():
        if entry.lower() == query.lower():
            return redirect("entry", title=query)
    
    pages = []
    for entry in util.list_entries():
        if query.lower() in entry.lower():

            pages.append(entry)

            ### TODO: CREATE RESULTS PAGE
            return render(request, "encyclopedia/results.html", {

                "pages": pages

            })
    else:
        return render(request, "encyclopedia/results.html")
    


def create(request):
    return render(request, "encyclopedia/create.html")


def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content =  request.POST["content"].strip()

        #if article already exists:
        for article in util.list_entries():
            if title.lower() == article.lower():
                return render(request, "encyclopedia/page_exist.html", {

                    "page": article

                })
            
        #create new article:
        util.save_entry(title, content)
        return redirect("entry", title=title)
        
def edit(request, title):

    title = title

    if request.method == "POST":
        content =  request.POST["content"].strip()
        util.save_entry(title, content)
        return redirect("entry", title=title)

    
    entry = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        
        "entry": entry,
        "title": title

    })
        
def random(request):

    entry = choice(util.list_entries())
    return redirect("entry", title=entry)
