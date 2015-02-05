from django.shortcuts import render,RequestContext,render_to_response


def submissionForm(request):
    return render_to_response('submissionForm.html',
            {'accepted':True},
            context_instance=RequestContext(request))
