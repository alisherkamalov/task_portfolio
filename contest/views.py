from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from .models import Participant

class ContestView(TemplateView):
    """Страница конкурса"""

    template_name = 'contest/contest.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        code_list = request.POST.getlist("code[]")  
        all_codes = '\n'.join(code_list) 

        # Создание нового участника
        participant = Participant(name=name, email=email, code=all_codes)
        participant.save()

        
        return redirect(f"{request.path}?success=true")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = Participant.objects.order_by('-created_at') 
        context['success'] = self.request.GET.get('success') == 'true'
        return context




