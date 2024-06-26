from django.contrib import admin
# Register your models here.
from django.contrib.admin import RelatedFieldListFilter
from django.utils.translation import gettext_lazy as _
from django_admin_listfilter_dropdown.filters import (RelatedDropdownFilter)

from exam.models import ExamType

from .models import FullLengthTest, createexam, module


@admin.register(FullLengthTest)
class Admin(admin.ModelAdmin):
    list_filter = ("name","reading_set", "listening_set", "speaking_set", "writing_set", "difficulty_level")
    search_fields = ("name","reading_set", "listening_set", "speaking_set", "writing_set", "difficulty_level")
    list_display = ["name", "reading_set", "listening_set", "speaking_set", "writing_set", "difficulty_level"]
    

class createexamadmin(admin.ModelAdmin):
    list_display = ("id", "ielts_names")
    list_filter = ("IELTS",)
    search_fields = ("IELTS",)

    def ielts_names(self, obj):
        return str(obj.IELTS.Name) if obj.IELTS else ""

class ExamTypeFilter(admin.SimpleListFilter):
    title = _('Exam Type')
    parameter_name = 'exam_type'

    def lookups(self, request, model_admin):
        return ExamType.choices

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(exam_type=self.value())


admin.site.register(createexam, createexamadmin)
# admin.site.register(Responses)
class RelatedDropdownFilter(RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin):
        limit_choices_to = getattr(self, 'limit_choices_to', {})
        related_model = getattr(field, 'remote_field').model
        qs = related_model._default_manager.complex_filter(limit_choices_to)
        return [(x.pk, str(x)) for x in qs]

class moduleadmin(admin.ModelAdmin):
    list_display = (
        "Name",
        "exam_test",
        "reading_list",
        "listening_list",
        "speaking_list",
        "writing_list",
        "awa_list",
        "integrated_reasoning_list",
        "quantitative_reasoning_list",
        "verbal_reasoning_list",
        "practice_test_type",
        "difficulty_level",
    )

    list_filter = ("Name","Reading", "Writing", "exam_test", "awa", "difficulty_level")
    search_fields = ("Namez","Reading", "Listening", "Writing", "exam_test", "awa", "difficulty_level")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        exam_type = request.GET.get('exam_type')  
        
        if exam_type:
            return queryset.filter(Reading__exam_type=exam_type)  
        return queryset

    def reading_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Reading.all()])

    def listening_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Listening.all()])

    def speaking_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Speaking.all()])

    def writing_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Writing.all()])

    def awa_list(self, obj):
        return ", ".join([str(exam) for exam in obj.awa.all()])

    def integrated_reasoning_list(self, obj):
        return ", ".join([str(exam) for exam in obj.integrated_reasoning.all()])

    def quantitative_reasoning_list(self, obj):
        return ", ".join([str(exam) for exam in obj.quantitative_reasoning.all()])

    def verbal_reasoning_list(self, obj):
        return ", ".join([str(exam) for exam in obj.verbal_reasoning.all()])


admin.site.register(module, moduleadmin)