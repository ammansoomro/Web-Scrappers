import webbrowser
with open("protected.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        line = line.rstrip('\n')
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(line)