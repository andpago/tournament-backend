from django.contrib import admin

from round.models import Round, Tournament


class RoundAdmin(admin.ModelAdmin):
    model = Round


class TournamentAdmin(admin.ModelAdmin):
    model = Tournament


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Round, RoundAdmin)
