from django.shortcuts import render, HttpResponse
import requests, datetime, json
from datetime import date
from .models import User_info

def index(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        data = {}

        for show_data in jsonList:
            data['id'] = show_data['id']
            data['name'] = show_data['name']
            data['public_gists'] = show_data['public_gists']
            data['public_repos'] = show_data['public_repos']
            data['followers'] = show_data['followers']
            data['following'] = show_data['following']

        for data in jsonList:
            #DELETE PREVIOUS ENTRY WITH SAME CREDENTIALS
            get_previous_entry=User_info.objects.filter(user_id=jsonList[0]['id'])
            get_previous_entry.delete()
            data_into_table = User_info(user_id=jsonList[0]['id'], username=str(jsonList[0]['login']),name=str(jsonList[0]['name']),
                                        public_gists=jsonList[0]['public_gists'], public_repos=jsonList[0]['public_repos'],
                                        followers=jsonList[0]['followers'], following=jsonList[0]['following'],
                                        image_for_thumbnail=jsonList[0]['avatar_url'], date_searched=date.today())
            data_into_table.save()
        parsedData.append(data)
    return render(request, 'app/profile.html', {'data': parsedData})