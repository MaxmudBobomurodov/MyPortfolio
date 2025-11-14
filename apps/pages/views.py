from django.views.generic import TemplateView

from apps.pages.models import AboutMe, Skills


class ViewPost(TemplateView):
    template_name = 'home-one.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.all()
        context['skills'] = Skills.objects.all()
        return context