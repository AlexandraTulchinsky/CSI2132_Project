from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


TEMPLATE_DIRS = (

    'os.path.join(BASE_DIR, "templates"),'
)

def home(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Users" WHERE "User_type" = \'Dentist\' OR "User_type" = \'Hygenist\' OR "User_type" = \'Hygienist\'')
        dentistRows = dictfetchone(cursor)

    context = {'dentistRows': dentistRows}
    return render(request, 'home.html', context)

def dictfetchone(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]