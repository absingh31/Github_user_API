from django.shortcuts import render, HttpResponse
import requests, json

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

        parsedData.append(data)
    return render(request, 'app/profile.html', {'data': parsedData})