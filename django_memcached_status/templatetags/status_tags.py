from django import template

register = template.Library()

@register.filter(name="from_sec_to_hm")
def from_sec_to_hm(seconds):
    sec = int(seconds)
    secs = sec % 60
    minutes = (sec / 60) % 60
    hours = (sec / (60 * 60))

    return "{0} hours {1} minutes {2} seconds".format(hours, minutes, secs)
from_sec_to_hm.is_safe = True
