from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from .models import Customer
from .forms import CustomerForm

class Create(generic.CreateView):
    model = Customer
    form_class = CustomerForm

    def form_valid(self, form):
        # フォームのデータは有効であると確認された後に呼び出される
        self.object = form.save(commit=False)  # データベースにはまだ保存しない
        self.object.calculate_credit_score()  # クレジットスコアを計算
        self.object.save()  # データベースに保存
        # 保存後のオブジェクトIDを使ってリダイレクト先のURLを動的に生成
        return redirect(reverse('credit:result', kwargs={'pk': self.object.pk}))

class List(generic.ListView):
    model = Customer
    paginate_by = 10

class Result(generic.TemplateView):
    template_name = 'credit/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs.get('pk')
        customer = Customer.objects.get(pk=customer_id)
        context['customer'] = customer
        return context
