from django.contrib import admin
from .models import Post, Category, Comment, UserProfile, Featured_Post

class LimitAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Featured_Post, LimitAdmin)
