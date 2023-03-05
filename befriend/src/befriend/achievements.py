from tkinter import N
import yaml

class Achievement:
    def __init__(self, id: str, name: str, overallProgress: int, currentProgress: int):
        self.id = id
        self.name = name
        self.overallProgress = overallProgress
        self.currentProgress = currentProgress

with open('befriend/src/befriend/resources/achievements.yml', 'r') as f: #wczytuje achievementy z yamla
    data = yaml.safe_load(f)

achievementlist = [] #achievementy beda po kolei
for element in data:
    id = element
    name = data[element]["name"]
    overallProgress = int(data[element]["overallProgress"])
    currentProgress = int(data[element]["currentProgress"])
    achievementlist.append(Achievement(id, name, overallProgress, currentProgress))
#kazdy achievement jako osobny obiekt
print(achievementlist[0].name)

def achievementGet():
    pass


def achievementProgress(num: int):
    achievementlist[num].currentProgress += 1
    if achievementlist[num].currentProgress == achievementlist[num].overallProgress:
        achievementGet()

