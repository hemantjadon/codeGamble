from django.conf.urls import url
from questions.views import *

urlpatterns = [
    url(r'^leaderboard/$',Leaderboard,name="leaderboard"),
    url(r'^move-next/$',MoveNext,name='move_next'),
    url(r'^leaderboard/get/$',LeaderboardGet,name="leaderboard_get"),
    url(r'^$',QuestionsPage,name='questions_page'),
    url(r'^winpage/$',WinPage,name='win_page'),
]