from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from apps.plans.models import Plan
from .forms import PlanForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import default_storage
import uuid

@csrf_protect
def upload_feature_icon(request):
    if request.method == "POST" and request.FILES.get("icon"):
        f = request.FILES["icon"]
        filename = f"feature_icons/{uuid.uuid4()}_{f.name}"
        path = default_storage.save(filename, f)
        return JsonResponse({"url": f"/media/{path}"})

    return JsonResponse({"error": "Invalid request"}, status=400)

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'plans/plan_list.html', {'plans': plans})


def plan_add(request):
    form = PlanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('plan_list')
    return render(request, 'plans/plan_form.html', {'form': form})

def plan_edit(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    form = PlanForm(request.POST or None, request.FILES or None, instance=plan)
    if form.is_valid():
        form.save()
        return redirect('plan_list')
    return render(request, 'plans/plan_form.html', {'form': form})


def plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('plan_list')
    return render(request, 'plans/plan_confirm_delete.html', {'plan': plan})
