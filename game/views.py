from django.shortcuts import RequestContext, render_to_response
from models import acceptWord,normalizeWord


def submissionForm(request):
    word = request.POST.get('word',None)
    score = -1
    if word is not None:
      if acceptWord(normalizeWord(word)):
          score = 1

    return render_to_response('submissionForm.html',
            {'score':score,
             'word':word},
            context_instance=RequestContext(request))
