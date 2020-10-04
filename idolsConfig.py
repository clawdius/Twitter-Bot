import random

hashtags = ['#아샤', '#이런', '#RYUJIN', '#YEJI', '#SIMYEONG', '#채솔', '#쥬리', '#연희', '#수윤']

idols = ['Aisha', 'Yiren', 'Ryujin', 'Yeji', 'Simyeong', 'Chaesol', 'Juri', 'Yeonhee', 'Suyun']

def randomIdols():
    maxLength = len(idols) - 1
    index = random.randint(0, maxLength)
    return idols[index]