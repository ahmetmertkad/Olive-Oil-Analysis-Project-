from django.shortcuts import render, redirect, get_object_or_404
from .forms import OliveOilForm
from django.contrib.auth.decorators import login_required
from .models import OliveOil
from django.contrib.auth import logout
import pandas as pd
from django.http import HttpResponse

def index(request):
    return render(request, 'HomePage.html')

def table(request):
    return render(request, 'table.html')

@login_required
def user_oils_view(request):
    olive_oils = OliveOil.objects.filter(user=request.user)
    return render(request, 'user_oils.html', {'olive_oils': olive_oils})

@login_required
def delete_oil(request, oil_id):
    if request.method == 'POST' and request.user.is_superuser:
        oil = get_object_or_404(OliveOil, id=oil_id)
        oil.delete()
        return redirect('user_oils_view')
    return redirect('user_oils_view')

@login_required
def styles(request):
    if request.method == 'POST':
        form = OliveOilForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('styles')
    else:
        form = OliveOilForm()

    all_olive_oils = OliveOil.objects.all()
    olive_oil_scores = []
    for oil in all_olive_oils:
        quality_score = oil.calculate_quality_score()
        olive_oil_scores.append({
            'name': oil.name,
            'oil_type': oil.get_oil_type_display(),
            'total_score': quality_score
        })

    return render(request, 'styles.html', {'form': form, 'olive_oil_scores': olive_oil_scores})

def search(request):
    query = request.GET.get('q')
    if query:
        olive_oil_scores = OliveOil.objects.filter(name__icontains=query)
    else:
        olive_oil_scores = []
    return render(request, 'search.html', {'olive_oil_scores': olive_oil_scores})

@login_required
def user(request):
    olive_oils = OliveOil.objects.filter(user=request.user)
    return render(request, 'user.html', {'olive_oils': olive_oils})

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def export_olive_oil_to_excel(request):
    olive_oil_data = OliveOil.objects.all()  # Fetch all OliveOil instances

    data = olive_oil_data.values( 
            'name', 
            'oil_type', 
            'acidity',
            'peroxide_value',
            'k232',
            'k270',
            'delta_k',
            'total_polyphenols',
            'moisture_and_volatiles',
            'pyropheophytins',
            'dag_content',
        )
    data = list(data)  # Convert QuerySet to a list of dictionaries
    for item in data:
        item['Quality Score'] = OliveOil.objects.get(name=item['name']).calculate_quality_score()  

    df = pd.DataFrame(data)
    
    # Create response object
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="all_olive_oils.xlsx"'

    # Write to Excel
    df.to_excel(response, index=False)

    return response
