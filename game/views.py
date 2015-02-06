from django.shortcuts import RequestContext, render_to_response
from models import acceptWord,normalizeWord,WordSubmission
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def submissionForm(request):
    word = request.POST.get('word',None)
    score = -1
    submission = None

    if word is not None:
      word = normalizeWord(word)
      if acceptWord(word):
          score = len(word);
          submission = WordSubmission(user=request.user,word=word,score=score)
          submission.save()

    orderedSubmissions = WordSubmission.objects.all().order_by('-score')
    
    overallHighscore = orderedSubmissions[:1]
    personalHighscore = orderedSubmissions.filter(user=request.user)[:1]
    top10 = orderedSubmissions.filter(submitted=date.today())[:10];

    return render_to_response('submissionForm.html',
            {'score':score,
             'word':word,
             'top10OfTheDay':top10,
             'personal_highscore':personalHighscore[0].score if len(personalHighscore)>0 else None,
             'overall_highscore':overallHighscore[0].score} if len(overallHighscore)>0 else None,
            context_instance=RequestContext(request))

