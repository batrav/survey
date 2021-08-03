from django import views
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import serializers
from .forms import SurveyForm
from .models import Survey
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .serializers import SurveyFormSerializers
# installed externally

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


def LandingPage(request):
    return HttpResponseRedirect("/new-survey/" + str(1))


def store_file_aws(file, file_name):
    with open("temp_aws/" + file_name, "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


def get_single_form_field(request):
    pass


class CreateSurveyView(View):

    def get(self, request, field_id):
        form = SurveyForm()
        survey_form = {
            1: 'first_name',
            2: 'last_name',
            3: 'email_id',
            4: "contact_no",
            5: "zip_code",
            6: "city",
            7: "own_house",
            8: "fully_vaccinated",
            9: "profile_icon",
            10: "vaccine_proof"
        }
        display_field = survey_form[field_id]
        # print(display_field)
        return render(request, 'survey/create_survey.html', {
            'form': form,
            "survey_form": survey_form,
            "display_field": display_field,
            "field_id": field_id,
            "next_field": field_id+1
        })

    def post(self, request, *args, **kwargs):

        submitted_form = SurveyForm(request.POST, request.FILES)
        survey_form = {
            1: 'first_name',
            2: 'last_name',
            3: 'email_id',
            4: "contact_no",
            5: "zip_code",
            6: "city",
            7: "own_house",
            8: "fully_vaccinated",
            9: "profile_icon",
            10: "vaccine_proof"
        }
        # print(type(int(request.path.split("/")[2]) + 1 ))
        id = request.path.split("/")[2]
        field_id = survey_form[int(id) - 1]
        if request.FILES.get(field_id) != None:
            request.session[field_id] = request.FILES.get(field_id).name
            store_file_aws(request.FILES.get(field_id),
                           request.FILES.get(field_id).name)
        else:
            request.session[field_id] = request.POST.get(field_id)
        print(f"############# {request.POST} ########## {request.FILES}")
        if int(request.path.split("/")[2]) <= 10:
            # print('success')
            # profile_icon = request.FILES['profile_icon']
            # print(profile_icon)
            return HttpResponseRedirect("/new-survey/" + (request.path.split("/")[2]))
        print(
            f'############# {[request.session.get(value) for id , value in survey_form.items()]}')
        # if int(request.path.split("/")[2]) == 11:
        #     # print('success')
        #     # return HttpResponseRedirect("/new-survey/"+ str(10))
        #     # print(submitted_form)
        #     submitted_form = SurveyForm(request.POST, request.FILES)
        #     vaccine_proof = request.FILES['vaccine_proof']
        #     print(vaccine_proof)
        #     print(submitted_form.is_valid())

        #     return HttpResponseRedirect("/thank-you")

        # print('################# - 9')
        print('yeahh')
        # print(request.POST['fully_vaccinated'])
        print(request.session.get)
        survey = Survey(first_name=request.session.get('first_name'),
                        last_name=request.session.get('last_name'),
                        email_id=request.session.get('email_id'),
                        contact_no=request.session.get('contact_no'),
                        zip_code=request.session.get('zip_code'),
                        city=request.session.get('city'),
                        own_house=True if request.session.get(
                            'own_house') == 'True' else False,
                        fully_vaccinated=True if request.session.get(
                            'fully_vaccinated') == 'True' else False,
                        profile_icon=request.session.get('profile_icon'),
                        vaccine_proof=request.session.get('vaccine_proof'))
        survey.save()

        # store_file_aws(request.FILES['profile_icon'],
        #                request.FILES['profile_icon'].name)
        # store_file_aws(
        #     request.FILES['vaccine_proof'], request.FILES['vaccine_proof'].name)

        return HttpResponseRedirect("/thank-you")

class ThankYouView(View):
    def get(self, request):
        return render(request, "survey/thanks.html")

class SurveyListView(ListView):
    template_name = 'survey/survey_list.html'
    model = Survey
    context_object_name = "surveys"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(first_name__isnull=False)
        data = base_query.filter(profile_icon__isnull=False)
        print(type(data))
        return data

class SurveyDetailView(DetailView):
    template_name = "survey/survey_detail.html"
    model = Survey

class SurveybyIDDetailView(View):
    def get(self, request):
        return render(request, "survey/survey_by_id.html")

    def post(self, request):
        req_id = request.POST.dict()
        survey_id = req_id.get("survey_id")
        print(survey_id)
        return HttpResponseRedirect("/survey/" + survey_id)

# def survey_edit(request, pk):
#     survey = get_object_or_404(Survey, pk=pk)
#     if request.method == "POST":
#         form = SurveyDetailView(request.POST, instance=survey)
#         if form.is_valid():
#             survey.save()
#             # return redirect('survey_detail', pk=survey.pk)
#     else:
#         form = SurveyForm(instance=survey)
#     return render(request, 'survey/create_survey.html', {'survey': survey})

class EditSurveyView(View):
    def get(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        form = SurveyForm(instance=survey)
        # print(form)
        return render(request, 'survey/edit_survey.html', {
            'form': form,
            "pk": pk
        })

    def post(self, request):
        submitted_form = SurveyForm(request.POST, request.FILES)
        print('in post')
        print(submitted_form.is_valid())
        # if submitted_form.is_valid():
        if submitted_form.is_valid():
            print('yeahh')
            print(request.POST['fully_vaccinated'])
            print(submitted_form.cleaned_data)
            # print(f"this is the id to edit {request.POST['survey_id']}")
            edit_survey = Survey.objects.get(pk=request.POST['survey_id'])
            print(edit_survey.id)
            edit_survey.first_name = submitted_form.cleaned_data['first_name']
            edit_survey.last_name = submitted_form.cleaned_data['last_name']
            edit_survey.email_id = submitted_form.cleaned_data['email_id']
            edit_survey.contact_no = submitted_form.cleaned_data['contact_no']
            edit_survey.zip_code = submitted_form.cleaned_data['zip_code']
            edit_survey.city = submitted_form.cleaned_data['city']
            edit_survey.own_house = submitted_form.cleaned_data['own_house']
            edit_survey.fully_vaccinated = submitted_form.cleaned_data['fully_vaccinated']
            edit_survey.profile_icon = request.FILES['profile_icon']
            edit_survey.vaccine_proof = request.FILES['vaccine_proof']

            edit_survey.save()

        if request.FILES:

            store_file_aws(request.FILES['profile_icon'],
                           request.FILES['profile_icon'].name)
            store_file_aws(
                request.FILES['vaccine_proof'], request.FILES['vaccine_proof'].name)

        return HttpResponseRedirect("/thank-you")

class ApiDataView(APIView):
    
    def get(self, request, *args, **kwargs):
        try: 
            # id = request.path.split("/")[2]
            id = request.GET['key']
            # print(request.path)  
            print(int(id))          
            if id !=None:
                survey_single = Survey.objects.get(pk=int(id))
                serializer = SurveyFormSerializers(survey_single)
                return Response(serializer.data)
        except:  
            print('in escept')          
            querys = Survey.objects.all()
            serializer = SurveyFormSerializers(querys, many=True)
            return Response(serializer.data)
            
    def post(self, request, *args, **kwargs):
        serializer  = SurveyFormSerializers(data=request.data)
        if serializer.is_valid():
            print('in post method')
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data)
            # queryset = Survey.objects.all()
        else:
            return Response(serializer.errors)
    
# from rest_framework import viewsets

# class ApiDataView(viewsets.ModelViewSet):
#     serializer_class = SurveyFormSerializers
#     queryset = Survey.objects.all()



# git@github.com:batrav/survey.git