from django import template

register = template.Library()

@register.filter
def find_writer(value, cid):
    for i in value:
        if i.idx == cid:
            ret = i.writer
    return ret