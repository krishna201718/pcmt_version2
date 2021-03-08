from django import template
from ..models import Subject
register = template.Library()


@register.filter
def index( indexable, i):
    print(indexable[i])
    return indexable[i]


@register.filter
def get_subject(subject_Id ):
    obj = Subject.object.get(subject=subject_Id)
    return obj.name