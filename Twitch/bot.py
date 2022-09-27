import requests
import json
import time
import os
import pandas as pd
client_id = 'yz7eopx1ewjnx0o3nb8zxbaitaxk1f'
client_secret = 'yvhb4cq3wysd4xdpbf47f3ck03m91d'
access_token = 'ewqaaj5lcxi8vxwe4dvropf0luurwg'
# Get Stream_ID Using username
def GetStreamInformation(username):
    output = ''
    url = 'https://api.twitch.tv/helix/streams?user_login=' + username
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    # print(data)
    user_id = data['data'][0]['user_id']
    url = 'https://api.twitch.tv/helix/streams?user_id=' + user_id
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    Live_Views = data.get('data')[0].get('viewer_count')
    Title = data.get('data')[0].get('title')
    output = output + Title.replace(',', '') + ',' +   str(Live_Views)
    return output


while(1):
    # Clear Screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Getting Data..... Please Wait")
    with open('Output.csv', 'w') as output:
        output.write("Status,Username,Title,Live Viewers,Time Stamp\n")
        with open('Links.txt', 'r') as file:
            for line in file:
                try:
                    username = line.strip().replace('https://www.twitch.tv/', '')
                    result = GetStreamInformation(username)
                    output.write("Live," + username + ',' + result + ',' +  time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
                except:
                    output.write("Offline," + username +  ',,,' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    # Close the file
    output.close()
    # Print the output.csv file using pandas
    df = pd.read_csv('Output.csv')
    print(df)
    time.sleep(60)