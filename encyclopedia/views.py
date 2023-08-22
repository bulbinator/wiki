from django.shortcuts import render
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
