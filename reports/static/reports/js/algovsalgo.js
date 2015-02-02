function refreshresults(choice){
//            Clear results
//            var results = document.getElementById("results");
//            results.innerHTML = "";
    var showallvids = document.getElementById("showallvids").checked;

    var selrun1 = document.getElementById("run1");
    var selval1 = selrun1.options[selrun1.selectedIndex].value;
    var cycle_id1 = selval1.split(',')[0];
    var algo1 = selval1.split(',')[1];

    var selrun2 = document.getElementById("run2");
    var selval2 = selrun2.options[selrun2.selectedIndex].value;
    var cycle_id2 = selval2.split(',')[0];
    var algo2 = selval2.split(',')[1];

//            var currentvideo = document.getElementById("currentvideo");
//            currentvideo.value = videoname;

    var data = cycle_id1 + '/' + cycle_id2;


    getvideos(cycle_id1, cycle_id2, choice, showallvids);

}

function createHeaderRow(choice) {

    var results = document.getElementById('results');


    var tablehead = document.createElement('thead');
    var headerrow = document.createElement('tr');

    var headercolgrp = document.createElement('th');
    headercolgrp.innerHTML = "grp";
    headerrow.appendChild(headercolgrp);
    var headercol1 = document.createElement('th');
    headercol1.innerHTML = "Video Name";
    headerrow.appendChild(headercol1);

    var headercol2 = document.createElement('th');
    headercol2.innerHTML = "play";
    headerrow.appendChild(headercol2);

    var headercol2 = document.createElement('th');
    headercol2.innerHTML = "id";
    headerrow.appendChild(headercol2);
    var headercol3 = document.createElement('th');
    headercol3.innerHTML = "cyc1";
    headerrow.appendChild(headercol3);
    var headercol4 = document.createElement('th');
    headercol4.innerHTML = "Exp1";
    headerrow.appendChild(headercol4);

    var headercol5 = document.createElement('th');
    headercol5.innerHTML = "Avg1";
    headerrow.appendChild(headercol5);
    var headercol6 = document.createElement('th');
    headercol6.innerHTML = "Var1";
    headerrow.appendChild(headercol6);
    var headercol7 = document.createElement('th');
    headercol7.innerHTML = "Fnl1";
    headerrow.appendChild(headercol7);

    var headercolid2 = document.createElement('th');
    headercolid2.innerHTML = "id2";
    headerrow.appendChild(headercolid2);
    var headercol11 = document.createElement('th');
    headercol11.innerHTML = "cyc2";
    headerrow.appendChild(headercol11);
    var headercol12 = document.createElement('th');
    headercol12.innerHTML = "Exp2";
    headerrow.appendChild(headercol12);

    var headercol13 = document.createElement('th');
    headercol13.innerHTML = "Avg2";
    headerrow.appendChild(headercol13);
    var headercol14 = document.createElement('th');
    headercol14.innerHTML = "Var2";
    headerrow.appendChild(headercol14);
    var headercol15 = document.createElement('th');
    headercol15.innerHTML = "Fnl2";
    headerrow.appendChild(headercol15);


    var headercol16 = document.createElement('th');
    headercol16.innerHTML = "Diff";
    headerrow.appendChild(headercol16);


    tablehead.appendChild(headerrow);
    results.appendChild(tablehead);
}


function createGridRow(video, i, choice){
    var tbody = document.getElementById('tbody');
    var headerrow = document.createElement('tr');
    var selavg1 = document.getElementById('selavg1');
    var selavg2 = document.getElementById('selavg2');
    var selavgnum1 = parseInt(selavg1.innerHTML);
    var selavgnum2 = parseInt(selavg2.innerHTML);

    if((i % 2) == 0){
        headerrow.className += " " + 'bg-success';
    }
    else{
        headerrow.className += " " + 'bg-warning';
    }
    var headercol0 = document.createElement('td');
    if(choice == 1) {
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.name = video.video_name1;
        checkbox.value = video.group;
        checkbox.id = 'vidchk' + video.video_id1;
        if (video.group == 'gone'){
            checkbox.checked = true;
        }
        var videoid = video.video_id1;
        var chkid = checkbox.id;
        checkbox.addEventListener('click', function(){
             setVideoGroup(1 , videoid, 'default', chkid);
        });
        headercol0.appendChild(checkbox);
    }
    else
    {
        headercol0.innerHTML = "na";
    }
    headerrow.appendChild(headercol0);


    var headercol1 = document.createElement('td');
    headercol1.innerHTML = video.video_name1;
    headerrow.appendChild(headercol1);
    var headercol2 = document.createElement('td');
    if(choice == 1) {
        var inputElement = document.createElement('input');
        inputElement.type = "button";
        inputElement.value = "play";
        inputElement.addEventListener('click', function(){
            startVideo(video.aws_output1,video.aws_output2, video.video_name1);
        });

        headercol2.appendChild(inputElement);
    }
     else
    {
        headercol2.innerHTML = "na";
    }
    headerrow.appendChild(headercol2);
    var headercol22 = document.createElement('td');
    headercol22.innerHTML = video.video_id1;
    headerrow.appendChild(headercol22);
    var headercol3 = document.createElement('td');
    headercol3.innerHTML = video.cycle_id1;
    headerrow.appendChild(headercol3);
    var headercol4 = document.createElement('td');
    headercol4.innerHTML = video.aexception1;
    headerrow.appendChild(headercol4);
    var headercol5 = document.createElement('td');
    var headercol6 = document.createElement('td');
    var headercol7 = document.createElement('td');
    if(choice == 1) {
        headercol5.innerHTML = video.average_score1;
        headercol6.innerHTML = video.variance_score1;
        headercol7.innerHTML = video.final_score1;
        if(video.aexception1 == 'good' && video.aexception2 == 'good') {
            selavgnum1 += parseInt(video.final_score1);
        }
    }
     else
    {
        headercol5.innerHTML = "na";
        headercol6.innerHTML = "na";
        headercol7.innerHTML = "na";
    }
    headerrow.appendChild(headercol5);
    headerrow.appendChild(headercol6);
    headerrow.appendChild(headercol7);

    var headercolvidid2 = document.createElement('td');
    headercolvidid2.innerHTML = video.video_id2;
    headerrow.appendChild(headercolvidid2);
    var headercol11 = document.createElement('td');
    headercol11.innerHTML = video.cycle_id2;
    headerrow.appendChild(headercol11);
    var headercol12 = document.createElement('td');
    headercol12.innerHTML = video.aexception2;
    headerrow.appendChild(headercol12);
    var headercol13 = document.createElement('td');
    var headercol14 = document.createElement('td');
    var headercol15 = document.createElement('td');
    var headercol16 = document.createElement('td');
    if(choice == 1) {
        headercol13.innerHTML = video.average_score2;
        headercol14.innerHTML = video.variance_score2;
        headercol15.innerHTML = video.final_score2;
        if(video.aexception1 == 'good' && video.aexception2 == 'good') {
            selavgnum2 += parseInt(video.final_score2);
        }
        headercol16.innerHTML = video.difference;
    }
     else
    {
        headercol13.innerHTML = "na";
        headercol14.innerHTML = "na";
        headercol15.innerHTML = "na";
        headercol16.innerHTML = "na";
    }
    headerrow.appendChild(headercol13);
    headerrow.appendChild(headercol14);
    headerrow.appendChild(headercol15);
    headerrow.appendChild(headercol16);

    selavg1.innerHTML = selavgnum1;
    selavg2.innerHTML = selavgnum2;

    tbody.appendChild(headerrow);
}

function getvideos(cycle_id1, cycle_id2, choice, showallvids){
    var maintable = document.getElementById("maintable");
    maintable.innerHTML = "";
    var selavg1 = document.getElementById('selavg1');
    var selavg2 = document.getElementById('selavg2');
    selavg1.innerHTML = 0;
    selavg2.innerHTML = 0;

    var results = document.createElement('table');
    results.id = 'results';
    results.class = 'display';
    results.cellspacing = "0";
    results.width = "100%";
    maintable.appendChild(results);

    var loading = document.getElementById('loading');
    loading.innerHTML = "Loading...";
    var ugroup = "";
    if( showallvids ){
        var ugroup = 'default';
    }
    else
    {
        var ugroup = 'gone';
    }

    var theUrl = cycle_id1 + '/' + cycle_id2 + '/' + ugroup;

    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {
            var videos = JSON.parse(xmlHttp.responseText);
//            sorted_videos = sortJsonArrayByProperty(videos, 'difference', -1);
            createHeaderRow(choice);

            var tbody = document.createElement('tbody');
            tbody.id = 'tbody';
            results.appendChild(tbody);
            var googVidCounter = 0;
            for (var i=0; i < videos.length; i++){
                if (videos[i].aexception1 == 'good' && videos[i].aexception2 == 'good'){
                    googVidCounter++;
                }
                if(showallvids || videos[i].group == 'default'){
                    createGridRow(videos[i],i, choice);
                }
            }
            selavg1.innerHTML = (parseInt(selavg1.innerHTML) / googVidCounter);
            selavg2.innerHTML = (parseInt(selavg2.innerHTML) / googVidCounter);
            var table = $('#results').DataTable({
                paging: false
            });
            new $.fn.dataTable.FixedHeader( table, {
                "offsetTop": 350
            } );

            loading.innerHTML = "";
        }
    };

    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send( null );
}

function sortJsonArrayByProperty(objArray, prop, direction){
    if (arguments.length<2) throw new Error("sortJsonArrayByProp requires 2 arguments");
    var direct = arguments.length>2 ? arguments[2] : 1; //Default to ascending

    if (objArray && objArray.constructor===Array){
        var propPath = (prop.constructor===Array) ? prop : prop.split(".");
        objArray.sort(function(a,b){
            for (var p in propPath){
                if (a[propPath[p]] && b[propPath[p]]){
                    a = a[propPath[p]];
                    b = b[propPath[p]];
                }
            }
            // convert numeric strings to integers
            a = a.match(/^\d+$/) ? +a : a;
            b = b.match(/^\d+$/) ? +b : b;
            return ( (a < b) ? -1*direct : ((a > b) ? 1*direct : 0) );
        });
        return objArray;
    }
}

function startVideo(url,url2, videoname){
    var myPlayer = document.getElementById("div_original");
    myPlayer.pause();
    myPlayer.setAttribute('src', "https://s3.amazonaws.com/homage-automation/Videos/" + videoname + "/" + videoname + ".mov");
//    myPlayer.innerHTML = '<source src="' + url + '" type="video/mp4">';
    myPlayer.load();
    myPlayer.play();

    var currentvideo = document.getElementById("currentvideo");
    currentvideo.value = videoname;

    var myPlayer = document.getElementById("div_video1");
    myPlayer.pause();
    myPlayer.setAttribute('src', url);
//    myPlayer.innerHTML = '<source src="' + url + '" type="video/mp4">';
    myPlayer.load();
    myPlayer.play();

    var myPlayer2 = document.getElementById("div_video2");
    myPlayer2.pause();
    myPlayer2.setAttribute('src', url2);
//    myPlayer.innerHTML = '<source src="' + url + '" type="video/mp4">';
    myPlayer2.load();
    myPlayer2.play();
}

function simultaneousPlayVideos(){
    var myPlayer = document.getElementById("div_video1");
    var myPlayer2 = document.getElementById("div_video2");
    myPlayer.pause();
    myPlayer2.pause();
    myPlayer.stop();
    myPlayer2.stop();
    myPlayer.play();
    myPlayer2.play();
}

//Download the video from S3
function DownloadRemake(button) {

    var currentvideo = document.getElementById("currentvideo");
    var movUrl = "https://s3.amazonaws.com/homage-automation/Videos/" + currentvideo.value + ".zip";

    var pom = document.createElement('a');
    pom.setAttribute('href', movUrl);
    pom.setAttribute('download', currentvideo.value + ".zip");
    pom.setAttribute('type', 'application/zip');
    pom.click();
}

function DownloadSelected(run_id){
    var currentvideo = document.getElementById("currentvideo");
    var selrun = document.getElementById(run_id);
    var selval = selrun.options[selrun.selectedIndex].value;
    var cycle_id = selval.split(',')[0];
    var algo = selval.split(',')[1];

    var movUrl = "https://s3.amazonaws.com/homage-automation/Output/" + algo + "/" + cycle_id + "/" + currentvideo.value + "/" + algo + "_" + cycle_id + "_" + currentvideo.value + "output.mp4";
    var plfUrl = "https://s3.amazonaws.com/homage-automation/Output/" + algo + "/" + cycle_id + "/" + currentvideo.value + "/" + algo + "_" + cycle_id + "_" + currentvideo.value + "output.plf";


    var pom = document.createElement('a');
    pom.setAttribute('href', movUrl);
    pom.setAttribute('download', algo1 + "_" + cycle_id1 + "_output" + ".mp4");
    pom.setAttribute('type', 'video/mp4');
    pom.click();

     var pom2 = document.createElement('a');
    pom2.setAttribute('href', plfUrl);
    pom2.setAttribute('download', algo1 + "_" + cycle_id1 + "_output" + ".plf");
    pom2.setAttribute('type', 'text/plain');
    pom2.click();
}

function setVideoGroup(choice , videoid, group, chkid){
   theUrl = "";
    var chkbx = document.getElementById(chkid);
    if( chkbx.checked ){
        var theUrl = videoid + '/' + 'gone';
    }
    else
    {
        var theUrl = videoid + '/' + 'default';
    }
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {
            alert('saved');
        }
    };

    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send( null );
}


function runAlgortihm(){

    algorunselect = document.getElementById('algorunselect');
    algoversion = algorunselect.options[algorunselect.selectedIndex].value;
    crashrunval = 0;
    optimizeval = 0;
    updatedbval = 0;
    var chkbxCrashrun = document.getElementById('crashrun');
    if( chkbxCrashrun.checked ){
        crashrunval = 1
    }
    var chkbxoptimize = document.getElementById('optimize');
    if( chkbxoptimize.checked ){
        optimizeval = 1
    }
    var chkbxupdatedb = document.getElementById('updatedb');
    if( chkbxupdatedb.checked ){
        updatedbval = 1
    }


    var theUrl = 'run_algo/' + crashrunval + '/' + optimizeval + '/' + updatedbval + '/' + String(algoversion);

    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {
            alert('finished running algorithm');
        }
    };

    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send( null );
}

function updateProgress(){

    var theUrl = 'get_progress/';

    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {
            var progress = JSON.parse(xmlHttp.responseText);
            algoprogress = document.getElementById('algorun_progress');
            progress_message = document.getElementById('progress_message');
            algoprogress.value = progress.algorun.value;
            algoprogress.max = progress.algorun.max;
            progress_message.innerHTML = progress.algorun.status;
        }
    };

    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send( null );
}



//runalgo/(?P<crashrun>0|1)/(?P<optimize>0|1)/(?P<updatedb>0|1)/(?P<algoversion>[

//$(document).ready(function(){
//
//
//
//});
