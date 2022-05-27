from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Game
from django.http import HttpResponseRedirect
from .forms import Reviewform
from django.urls import reverse

# Create your views here.


class startingPageView(ListView):
    template_name = 'gamebit/home.html'
    model = Game
    ordering = ['-date']
    context_object_name = "games"

    def get_queryset(self):
        querySet = super().get_queryset()
        data = querySet[:4]
        return data
    

class storePageView(ListView):
    template_name = "gamebit/store.html"
    model = Game
    ordering = ['-date']
    context_object_name= "all_games"

class Gamedetails(View):
    def for_library(self,request, game_id):
        stored_in_library= request.session.get("stored_in_library")
        if stored_in_library is not None:
            for_library = game_id in stored_in_library
        else:
            for_library = False

        return for_library

    def get(self,request, slug):
        game = Game.objects.get(slug=slug)
        context = {
            "game" : game,
            "review_form": Reviewform(),
            "reviews": game.reviews.all(),
            "for_library": self.for_library(request, game.id)
        }
        return render(request,"gamebit/game-detail.html",context)

    def post(self,request, slug):
        review_form = Reviewform(request.POST)
        game = Game.objects.get(slug=slug)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.game = game
            review.save()
            return HttpResponseRedirect(reverse("game-detail",args=[slug]))
        context = {
            "game" : game,
            "review_form": Reviewform(),
            "reviews": game.reviews.all(),
            "for_library": self.for_library(request, game.id)
        }   
        return render(request,"gamebit/game-detail.html",context)

    

class Library(View):
    def get(self, request):
        stored_in_library= request.session.get("stored_in_library")
        context={}
        if stored_in_library is None or len(stored_in_library)== 0:
            context["games"]=[]
            context["has_games"]= False
        else:
            games = Game.objects.filter(id__in=stored_in_library)
            context["games"] = games
            context["has_games"] = True
        return render(request,"gamebit/library.html",context)
    def post(self, request):
        stored_in_library = request.session.get("stored_in_library")
        if stored_in_library is None:
            stored_in_library = []
        game_id = int(request.POST["game_id"])
        if game_id not in stored_in_library:
            stored_in_library.append(game_id)
        else:
            stored_in_library.remove(game_id)
        request.session["stored_in_library"] = stored_in_library
        return HttpResponseRedirect("/")

