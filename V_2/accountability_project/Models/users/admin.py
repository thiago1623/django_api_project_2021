from django.contrib import admin
from Models.users.models import User
from Models.groups.models import Group, Post
from Models.scoreboards.models import ScoreBoard
from Models.habits.models import Habit, StartDay, FinishDay


admin.site.register(User)
admin.site.register(Group)
admin.site.register(Post)
admin.site.register(ScoreBoard)
admin.site.register(Habit)
admin.site.register(StartDay)
admin.site.register(FinishDay)
