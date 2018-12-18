import webbrowser
keywords = ['python','javascript','youtube','kospi']
for keyword in keywords:
url= 'https://www.google.com/search?q=' + keyword
webbrowser.open_new(url)   