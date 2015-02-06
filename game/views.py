from django.shortcuts import RequestContext, render_to_response
from models import acceptWord,normalizeWord,WordSubmission
from django.contrib.auth.decorators import login_required

@login_required
def submissionForm(request):
    word = request.POST.get('word',None)
    score = -1
    submission = None

    if word is not None:
      if acceptWord(normalizeWord(word)):
          score = 1
          submission = WordSubmission(user=request.user,word=word,score=score)
          submission.save()

    return render_to_response('submissionForm.html',
            {'score':score,
             'word':word},
            context_instance=RequestContext(request))
