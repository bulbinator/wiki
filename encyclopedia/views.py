from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title)
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