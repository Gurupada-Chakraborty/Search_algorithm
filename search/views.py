from django.shortcuts import render
from django.contrib import messages
from .models import Words
import csv
import io
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('admin.can_add_log_entry')
def data_upload(request):
    template = 'data_upload.html'

    prompt = {
        'sequence': 'Order should be Words, Frequency',
    }
    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a .csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Words.objects.update_or_create(
            word=column[0],
            frequency=column[1]
        )
    context = {}
    return render(request, template, context)


