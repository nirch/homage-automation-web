from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
import simplejson

from reports.model.models import Crashrun, UploadFileForm, DocumentForm, Document
from reports.octopus import octopus
from reports.octopus.octopus import handle_uploaded_file
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    # cr_list = octopus.get_crash_runs()
    template = loader.get_template('reports/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def crashrun(request, cycle_id):
    try:
        cr = octopus.get_crash_run_by_cycle(cycle_id)
    except Crashrun.DoesNotExist:
        raise Http404
    return render(request, 'reports/crashrun.html', {'crashrun': cr})

def algovsalgo(request, choice):
    r = None
    runlist = []
    if choice == '0':
        r = octopus.get_crash_runs()
        for run in r:
            jsonrun = {}
            jsonrun['cycle_id'] = run.cycle_id
            jsonrun['algo_version'] = run.algo_version
            jsonrun['params'] = run.params
            jsonrun['start_date'] = run.start_date
            jsonrun['end_date'] = run.end_date
            jsonrun['crash_count'] = run.crash_count
            runlist.append(jsonrun)
    elif choice == '1':
        r = octopus.get_auto_runs()
        for run in r:
            jsonrun = {}
            jsonrun['cycle_id'] = run.cycle_id
            jsonrun['algo_version'] = run.algo_version
            jsonrun['params'] = run.params
            jsonrun['start_date'] = run.start_date
            jsonrun['end_date'] = run.end_date
            jsonrun['avg_score'] = "{:10.2f}".format(run.avg_score)
            jsonrun['crash_count'] = run.crash_count
            runlist.append(jsonrun)
    else:
        raise Http404
    videogroups = octopus.get_video_groups()
    return render(request, 'reports/algovsalgo.html', {'runlist':runlist, 'choice':choice, 'videogroups':videogroups})

def get_videos(request, choice, cycle_id1, cycle_id2, group):
    videos = []
    if choice == '0':
        videos = octopus.get_crash_run_videos(cycle_id1, cycle_id2)
    elif choice == '1':
        videos = octopus.get_auto_run_videos(cycle_id1, cycle_id2, group)
    return HttpResponse(simplejson.dumps(videos), content_type = "application/json")


def set_video_group(request, choice, video_id, group):
    status = ''
    try:
        octopus.set_video_group(choice, video_id, group)
        status = 'good'
    except Crashrun.DoesNotExist:
        status = 'bad'

# def download_video(request, video_name):
#     video = octopus.get_video(video_name)
    return HttpResponse(status, content_type = "text/plain")


# def upload_file(request):
#     form = None
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     return render_to_response('reports/index.html', {'form': form})


def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # newdoc = Document(docfile = request.FILES['docfile'])
            # newdoc.save()

            docfile = request.FILES['docfile']
            handle_uploaded_file(docfile)

            # Redirect to the document list after POST
            # return HttpResponseRedirect('reports/index.html')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'reports/index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )