from django.contrib import admin

from django import forms

from blog.models import Blog, Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ['blog', 'date', 'author', 'title', 'text']
    list_display = ['title', 'author', 'date']
    
    def formfield_for_dbfield(self, db_field, **kwargs):
            formfield = super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs)
            if db_field.name == 'text':
                formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            return formfield


class EntryInline(admin.StackedInline):
    model = Entry
    
    def formfield_for_dbfield(self, db_field, **kwargs):
            formfield = super(EntryInline, self).formfield_for_dbfield(db_field, **kwargs)
            if db_field.name == 'text':
                formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            return formfield


class BlogAdmin(admin.ModelAdmin):
    inlines = [EntryInline, ]
    
    
    


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)