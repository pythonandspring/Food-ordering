from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from .models import Student


# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'home/student_detail.html', {'student': student})

# class customerListView(generic.ObjectListView):
#     queryset = Provider.objects.annotate(
#         count_circuits=count_related(Circuit, 'provider')
#     )
#     filterset = filtersets.ProviderFilterSet
#     filterset_form = forms.ProviderFilterForm
#     table = tables.ProviderTable

# class customerView(GetRelatedModelsMixin, generic.ObjectView):
#     queryset = Provider.objects.all()

#     def get_extra_context(self, request, instance):
#         return {
#             'related_models': self.get_related_models(request, instance),
#         }

# class customerEditView(generic.ObjectEditView):
#     queryset = Provider.objects.all()
#     form = forms.ProviderForm


# class customerDeleteView(generic.ObjectDeleteView):
#     queryset = Provider.objects.all()
