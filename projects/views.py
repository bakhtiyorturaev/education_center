from django.shortcuts import redirect, render
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def projects(request):
    projects_list = Project.objects.filter(project_review__isnull=True)

    page_number = request.GET.get('page')
    paginator = Paginator(projects_list, 3)
    projects = paginator.get_page(page_number)

    reviews_p = Review.objects.filter(value="+")
    reviews_m = Review.objects.filter(value="-")

    max_pages = paginator.num_pages
    current_page = projects.number
    start_page = max(current_page - 5, 1)
    end_page = min(current_page + 4, max_pages)
    page_numbers = range(start_page, end_page + 1)

    context = {
        "projects": projects,
        "reviews_p": reviews_p,
        "reviews_m": reviews_m,

        "page_numbers": page_numbers,
        "max_pages": max_pages,
        "current_page": current_page
    }
    return render(request, "projects/projects.html", context)


def project(request, id):
    project = Project.objects.get(id=id)
    tags = project.tag.all()
    context = {
        "project": project,
        "tags": tags
    }
    return render(request, "projects/project.html", context)


@login_required(login_url='login')
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profil
            project.save()
            return redirect('projects')
    form = ProjectForm()
    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)


@login_required(login_url='login')
def project_edit(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }
    return render(request, "projects/project_add.html", context)


@login_required(login_url='login')
def project_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')
