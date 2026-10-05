from django.contrib import admin
from .models import Material, Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 4  # Har bir test yaratilganda bir yo'la 4 ta savol maydonini chiqaradi

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    inlines = [QuestionInline]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_at')

admin.site.register(Question)