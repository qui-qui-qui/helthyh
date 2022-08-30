from django import template
register = template.Library()

@register.filter
def create_range(value, start_index=0):
    return range(start_index, value+start_index)

@register.filter
def divide(value, divided):
    return value//divided + 1

@register.filter
def multiply(value, multiplyded):
    return value*multiplyded

    #  and i|multiply:7|add:j|add:1 >= day.numeric
    # <td><a class="scnd-font-color" href="#100">{{i|multiply:7|add:j|add:1}}</a></td>