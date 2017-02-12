from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from tasks.models import Task


# Create your views here.
class HomepageView(TemplateView):
    """
    The Homepage View.
    """
    template_name = "index.html"


class ContactView(TemplateView):
    """
    The Contact Us View.
    """
    template_name = "core/contact.html"


class AboutView(TemplateView):
    """
    The About Us View.
    """
    template_name = "core/about.html"


@login_required
def ActView(request):
    """
    The Act View.
    """
    template_name = "core/act.html"
    task_list = Task.objects.filter(user=request.user, is_archived=False)
    return render(request, template_name, {'tasks': task_list})


class MeetTheTeam(TemplateView):
    """
    Meet The Team View.
    """
    template_name = "core/team.html"


class TermsAndConditions(TemplateView):
    """
    Terms And Conditions View.
    """
    template_name = "core/terms_and_conditions.html"


class ThinkView(TemplateView):
    """
    The Think View.
    """
    template_name = "core/think.html"
