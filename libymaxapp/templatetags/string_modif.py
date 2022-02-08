from django import template

import re
register = template.Library()

def date_modif(value):
    res = re.sub("T.*Z", "", value)
    return res

register.filter('date_modif', date_modif)
register.tag('')