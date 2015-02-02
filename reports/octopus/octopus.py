import os
from reports.networking import aws_helper
from reports.octopus import consts
import time

__author__ = 'dangalg'
from reports.model.models import Crashrun, Autorun, Crashrunvideo, Autorunvideo, Videos, UploadFileForm


def get_crash_runs():
    cr_list = Crashrun.objects.order_by('-algo_version')[:10]
    return cr_list


def get_auto_runs():
    ar_list = Autorun.objects.order_by('-algo_version')[:10]
    return ar_list


def handle_uploaded_file(f):
    # create folder on local computer
    algo_folder_name = time.strftime("/media/v-%y-%m-%d/")
    aws_folder_name = time.strftime("/v-%y-%m-%d/")
    if not os.path.exists(algo_folder_name):
        os.makedirs(algo_folder_name)
    # Create file on local computer
    algo_file_name = 'UniformMattingCA.exe'

    with open(algo_folder_name + algo_file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    aws_helper.uploadfiletos3(consts.awsautomationbucket,
                              consts.awsalgorithem + aws_folder_name + algo_file_name, algo_folder_name + algo_file_name)

    # os.remove(algo_folder_name)


def get_auto_run_videos(cycle_id1, cycle_id2, ugroup):
    ar_list1 = Autorunvideo.objects.filter(cycle=cycle_id1).order_by('video_id')
    ar_list2 = Autorunvideo.objects.filter(cycle=cycle_id2).order_by('video_id')
    jsonvids = []
    i = -1
    filtervideos= False
    if(ugroup == 'gone'):
        filtervideos= True
    for vid in ar_list1:
        i += 1
        if(vid.video.group == 'default' or not filtervideos):
            jsonvid = {}
            jsonvid['runvideo_id1'] = vid.autorunvideo_id
            jsonvid['group'] = vid.video.group
            jsonvid['cycle_id1'] = vid.cycle.cycle_id
            jsonvid['video_id1'] = vid.video.video_id
            jsonvid['video_name1'] = vid.video.video_name
            jsonvid['average_score1'] = "{:10.2f}".format(vid.average_score)
            jsonvid['aexception1'] = vid.avexception
            jsonvid['variance_score1'] = "{:10.2f}".format(vid.variance_score)
            jsonvid['final_score1'] = "{:10.2f}".format(vid.final_score)
            jsonvid['aws_output1'] = vid.aws_output

            jsonvid['runvideo_id2'] = ar_list2[i].autorunvideo_id
            jsonvid['cycle_id2'] = ar_list2[i].cycle.cycle_id
            jsonvid['video_id2'] = ar_list2[i].video.video_id
            jsonvid['video_name2'] = ar_list2[i].video.video_name
            jsonvid['average_score2'] = "{:10.2f}".format(ar_list2[i].average_score)
            jsonvid['aexception2'] = ar_list2[i].avexception
            jsonvid['variance_score2'] = "{:10.2f}".format(ar_list2[i].variance_score)
            jsonvid['final_score2'] = "{:10.2f}".format(ar_list2[i].final_score)
            jsonvid['aws_output2'] = ar_list2[i].aws_output

            if vid.avexception == 'good' and ar_list2[i].avexception == 'good':
                jsonvid['difference'] = "{:10.2f}".format(vid.final_score - ar_list2[i].final_score)
            else:
                jsonvid['difference'] = 0
            jsonvids.append(jsonvid)
    return jsonvids


def get_crash_run_videos(cycle_id1, cycle_id2):
    ar_list1 = Crashrunvideo.objects.filter(cycle=cycle_id1)
    ar_list2 = Crashrunvideo.objects.filter(cycle=cycle_id2)
    jsonvids = []
    i = -1
    for vid in ar_list1:
        i += 1
        jsonvid = {}
        jsonvid['runvideo_id1'] = vid.crashrunvideo_id
        jsonvid['group'] = vid.video.group
        jsonvid['cycle_id1'] = vid.cycle.cycle_id
        jsonvid['video_id1'] = vid.video.video_id
        jsonvid['video_name1'] = vid.video.video_name
        jsonvid['aexception1'] = vid.crvexception

        jsonvid['runvideo_id2'] = ar_list2[i].crashrunvideo_id
        jsonvid['cycle_id2'] = ar_list2[i].cycle.cycle_id
        jsonvid['video_id2'] = ar_list2[i].video.video_id
        jsonvid['video_name2'] = ar_list2[i].video.video_name
        jsonvid['aexception2'] = ar_list2[i].crvexception

        jsonvids.append(jsonvid)
    return jsonvids

def get_crash_run_by_cycle(cycleid):
    return Crashrun.objects.get(pk=cycleid)

def set_video_group(choice, uvideo_id, ugroup):
    Videos.objects.select_related().filter(video_id=uvideo_id).update(group=ugroup)

def get_video_groups():
    return Videos.objects.values('group').distinct()