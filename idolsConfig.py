import random

hashtags = [
    '#아샤', '#이런', '#류진', '#예지', '#시명', '#채솔', '#쥬리', '#연희', '#수윤', '#조이', '#JIHYO', '#지수', '#채령', '#유나', '#시현', '#미나', '#모모'
    ]

idols = [
    'Aisha', 'Yiren', 'Ryujin', 'Yeji', 'Simyeong', 'Chaesol', 'Juri', 'Yeonhee', 'Suyun', 'Joy', 'Jihyo', 'Jisoo', 'Chaeryeong', 'Yuna', 'Sihyeon', 'Mina', 'Momo' 
    ]

def randomIdols():
    maxLength = len(idols) - 1
    index = random.randint(0, maxLength)
    return idols[index]