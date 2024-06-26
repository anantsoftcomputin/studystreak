# master/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import LessonAssignment

from .models import (
    Category,
    City,
    Country,
    CourseOverview,
    Cupon,
    ExamType,
    Language,
    Level,
    ModuleType,
    Outcomes,
    PackageType,
    QuestionType,
    Requirements,
    Section,
    SEOMetakeywords,
    State,
    TestType,
    batch,
    Live_Class_Type,
)


@admin.register(TestType)
class TestTypeAdmin(admin.ModelAdmin):
    list_filter = ["test_type"]
    search_fields = ["test_type"]
    list_display = ["test_type"]


@admin.register(ModuleType)
class ModuleTypeAdmin(admin.ModelAdmin):
    list_filter = ["module_type"]
    search_fields = ["module_type"]
    list_display = ["module_type"]


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    list_filter = ["exam_type"]
    search_fields = ["exam_type"]
    list_display = ["exam_type"]


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_filter = ["question_type"]
    search_fields = ["question_type"]
    list_display = ["question_type"]

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name",]


@admin.register(Level)
class LevelAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name",]


@admin.register(Requirements)
class RequirementsAdmin(ImportExportModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]
    list_filter = ["description", ]


@admin.register(Outcomes)
class OutcomesAdmin(ImportExportModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]
    list_filter = ["description"]

@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

@admin.register(CourseOverview)
class CourseOverviewAdmin(ImportExportModelAdmin):
    list_display = ["overview"]
    search_fields = ["overview"]
    list_filter = ["overview"]


@admin.register(SEOMetakeywords)
class SEOMetakeywordsAdmin(ImportExportModelAdmin):
    list_display = ["keywords"]
    search_fields = ["keywords"]
    list_filter = ["keywords"]


@admin.register(PackageType)
class PackageTypeAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(batch)
class batchAdmin(ImportExportModelAdmin):
    list_display = [
        "batch_name",
        "batch_startdate",
        "batch_enddate",
        "batch_start_timing",
        "batch_end_timing",
    ]
    search_fields = [
        "batch_name",
        "batch_startdate",
        "batch_enddate",
        "batch_start_timing",
        "batch_end_timing",
    ]
    list_filter = [ "batch_name",
        "batch_startdate",
        "batch_enddate",
        "batch_start_timing",
        "batch_end_timing",]


@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ['id', 'cupon_name', 'campaign_name', 'cupon_code', 'discount', 'start_date', 'end_date']
    list_filter = ['cupon_name', 'campaign_name', 'cupon_code']
    search_fields = ['cupon_name', 'campaign_name', 'cupon_code']

class LessonAssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson']
    list_filter = ["lesson"]
    search_fields = ["lesson"]

admin.site.register(LessonAssignment, LessonAssignmentAdmin)

admin.site.register(Live_Class_Type)