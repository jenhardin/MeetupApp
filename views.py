import json
import requests
from django.shortcuts import render, redirect
from django.views import generic
import urllib.request
#from .forms import MeetupForm
import datetime
from django.http import HttpResponse
import os


with open('static/json/meetups.json') as json_file:
    meetupData = json.load(json_file)

with open('static/json/jsonUpdateMeetup.json') as updatedjson_file:
    jsonUpdatedFile = json.load(updatedjson_file)
    

filteredLinks = []



# ******** This section is to be commented out until the urls in meetups.json work again ***********
def meetup(request):
    # lastDate = datetime.datetime.utcfromtimestamp(  os.path.getmtime('static/json/jsonUpdateMeetup.json') ).date() #The saved date of json file
    # time = datetime.datetime.today().date() #Today's date
    # # checking time on computer to see if json file needs to be updated, only needed once per day so load time is quicker
    # if lastDate != time:
    #     for links in meetupData["meetupURLS"]:
    #         openURLS = urllib.request.urlopen(links)
    #         datas = openURLS.read()
    #         datas = json.loads(datas)
    #         # checking if url has data for future event, if it is empty then don't add to filteredLinks
    #         if len(datas) != 0:
    #             array = []
    #             array.append(datas)
    #             filteredLinks.append(array)

    #     with open('static/json/jsonUpdateMeetup.json', "r") as f:
    #         data = json.load(f)
    #     data = filteredLinks
    #     # rewrite json file with updated information from API list, also formatting for more readability
    #     with open('static/json/jsonUpdateMeetup.json', "w") as f:
    #         json.dump(data, f, indent = 4, sort_keys = True)

    #     lastDate = time
        return GroupsWithEvents(request)

    # else:

    #     return GroupsWithEvents(request)

MeetupGroupNameList = []


def GroupsWithEvents(request):
    # keeps dropdown group names from duplicating upon refreshing page
    MeetupGroupNameList.clear()
    # creating list of group names for dropdown menu
    index = 0   
    while index < len(jsonUpdatedFile):
        MeetupGroupNameList.append(jsonUpdatedFile[index][0][0]['group']['name'])
        index += 1

    context = {'MeetupGroupNameList': MeetupGroupNameList}
    
    return render(request, 'MeetupApp/MeetupApp.html', context)


def GroupName(request, name):
    eventInfoUpdate = []
    selectedIndex = 0
    i = 0
    while i < len(MeetupGroupNameList):
        # creating index of selected group name to match up with index of its correlated events
        if MeetupGroupNameList[i] == name:
            selectedIndex = i
        i += 1

    for i in range(len(jsonUpdatedFile[selectedIndex][0])):
        # dictionary to add selected group name and event info to then add to html page template tags
        eventInfo = {
            'eventGroupName': None,
            'eventName' : None,
            'eventAddress' : None,
            'eventLink' : None,
        }
        eventGroupName = jsonUpdatedFile[selectedIndex][0][i]["group"]["name"]
        eventName = jsonUpdatedFile[selectedIndex][0][i]["name"]
        eventDate = jsonUpdatedFile[selectedIndex][0][i]["local_date"]
        eventTime = jsonUpdatedFile[selectedIndex][0][i]["local_time"]
        eventAddress = jsonUpdatedFile[selectedIndex][0][i]['venue']['address_1']
        eventLink = jsonUpdatedFile[selectedIndex][0][i]['link']
        eventInfo.update(eventGroupName = eventGroupName, eventName = eventName, eventDate = eventDate, eventTime = eventTime, eventAddress = eventAddress, eventLink = eventLink)
        eventInfoUpdate.append(eventInfo)

    context = {
        'eventInfoUpdate': eventInfoUpdate,
        'MeetupGroupNameList': MeetupGroupNameList
 
    }
    
    return render(request, 'MeetupApp/MeetupApp.html', context)

