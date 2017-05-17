from django.shortcuts import render, HttpResponse
import requests, datetime, json
from datetime import date
from .models import User_info

def index(request):
    parsedData = []
    if request.method == 'POST':
        username, jsonList = request.POST.get('user'), []                #REQUIRED DECLARATIONS
        req = requests.get('https://api.github.com/users/' + username)   #GET THE USER DATA
        jsonList.append(json.loads(req.content))                         #MAKE LIST OF DATA

        for data in jsonList:
            #Applying changes to database for given API request, updating when a user's data is requested again
            get_previous_entry=User_info.objects.filter(user_id=jsonList[0]['id'])
            get_previous_entry.delete()                                  #DELETES PREVIOUS ENTRY OF SAME USER
            data_into_table = User_info(user_id=jsonList[0]['id'], username=str(jsonList[0]['login']),name=str(jsonList[0]['name']),
                                        image_for_thumbnail=jsonList[0]['avatar_url'], public_gists=jsonList[0]['public_gists'],
                                        public_repos=jsonList[0]['public_repos'], followers=jsonList[0]['followers'],
                                        following=jsonList[0]['following'], date_searched=date.today())       #APPLY CHANGES TO MODEL VARIABLES
            data_into_table.save()                                       #SAVE DATA OF USER IN DATABASE
        parsedData.append(data)

    return render(request, 'app/profile.html', {'data': parsedData})
