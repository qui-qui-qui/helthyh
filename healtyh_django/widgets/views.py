from django.shortcuts import render
import datetime
from calendar import monthrange

# Create your views here.
def calendar_widget_calculating():
    date = datetime.datetime.now()
    
    context = {
        'month': date.strftime("%B"),
        'day': {
            'numeric': date.day,
            'letter': date.strftime("%A"),
            'weekday': datetime.datetime.today().weekday()
        },
        'year': date.year
    }

    days = monthrange(context['year'], date.month)[1]
    context['days'] = days
    #td_first = date.numeric
    return context