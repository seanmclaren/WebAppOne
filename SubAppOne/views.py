from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "appmain.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class AppCollectionPageView(TemplateView):
    template_name = "appcollection.html"
