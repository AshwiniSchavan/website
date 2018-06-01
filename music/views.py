from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album,Song
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):

    model = Album
    fields = ['artist', 'album_title ', ' genre', ' album_logo']


class AlbumUpdate(UpdateView):

    model = Album
    fields = ['artist', 'album_title ', ' genre', ' album_logo']


class AlbumDelete(DeleteView):

    model = Album
    success_url = reverse_lazy('music:index')


def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})