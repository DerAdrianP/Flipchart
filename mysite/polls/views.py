from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib import messages

from datetime import datetime
from .models import Choice,Question
from .forms import QuestionForm,ChoiceForm

from django.core.paginator import Paginator
from django.db.models import Q

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def index(request):
    queryset1 = Question.objects.filter(status=Question.STATUS_0).order_by('-pub_date')
    queryset2 = Question.objects.filter(status=Question.STATUS_1).order_by('-pub_date')
    queryset3 = Question.objects.filter(status=Question.STATUS_2).order_by('-pub_date')
    
    keyword = request.GET.get('keyword')
    if keyword and not keyword=='':
        splits = keyword.split(' ')
        for key in splits:
            queryset1 = queryset1.filter(question_text__contains=key)
            queryset2 = queryset2.filter(question_text__contains=key)
            queryset3 = queryset3.filter(question_text__contains=key)
    else:
        keyword = ''

    paginator1 = Paginator(queryset1, 5) # Show 5 items per page by default
    page1 = request.GET.get('page1')
    if not page1:
        page1 = 1

    paginator2 = Paginator(queryset2, 5) # Show 5 items per page by default
    page2 = request.GET.get('page2')
    if not page2:
        page2 = 1

    paginator3 = Paginator(queryset3, 5) # Show 5 items per page by default
    page3 = request.GET.get('page3')
    if not page3:
        page3 = 1

    question_list1 = paginator1.get_page(page1)
    question_list2 = paginator2.get_page(page2)
    question_list3 = paginator3.get_page(page3)

    context = {
        'question_list1': question_list1,
        'question_list2': question_list2,
        'question_list3': question_list3,
        'keyword': keyword,
    }
    return render(request,"polls/index.html",context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.status!=question.STATUS_1:
         return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You cannot vote in this status .",
        })
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        for choice in question.choice_set.all():
            choice.voters.remove(request.user)
        selected_choice.voters.add(request.user) 
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def addQuestion(request):
    # print(datetime.now())
    if request.method == 'POST':
        form = QuestionForm(request.POST)    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pub_date = datetime.now()
            instance.creator = request.user
            instance.save()

            agree = Choice()
            agree.choice_text = 'Agree'
            agree.question = instance
            agree.save()

            disagree = Choice()
            disagree.choice_text = 'Disagree'
            disagree.question = instance
            disagree.save()

            messages.success(request, "New Card Created!")
            return redirect('index')
        else:
            return render(request,'form_action.html',{'form':form})
    else:
        form = QuestionForm()
        return render(request,'form_action.html',{'form':form})

def deleteQuestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('index')
    
def editQuestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(datetime.now())
    if request.method == 'POST':
        form = QuestionForm(request.POST,instance=question)    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pub_date = datetime.now()
            instance.creator = request.user
            instance.save()
            messages.success(request, "New Card Created!")
            return redirect('index')
        else:
            return render(request,'form_action.html',{'form':form})
    else:
        form = QuestionForm(instance=question)
        return render(request,'form_action.html',{'form':form})

        
def download(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString( 30,800,"von   "+str(question.creator))
    p.drawString( 30,780,str(question.pub_date))
    p.drawString( 30,760,str(question.question_text ))
   
    height=640
    for choice in question.choice_set.all():
        p.drawString( 30,height,choice.choice_text+" -- "+str(choice.voters.count())+ " vote(s)")
        height=height-20
        voters=""
        for voter in choice.voters.all():
            voters=voters+str(voter)+", "
        p.drawString( 30,height,voters)
        height=height-60


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='card.pdf')