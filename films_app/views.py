from django.shortcuts import render
from .data_analysis import analyze_actor_films

# Create your views here.
def actor_info(request):
    if request.method == 'POST':
        actor_id = int(request.POST['actor_id'])
        actor_name, films_per_category = analyze_actor_films(actor_id)

        context = {
            'actor_name': actor_name,
            'films_per_category': films_per_category.to_html(index=False),
        }
        return render(request, 'result.html', context)

    return render(request, 'index.html')

