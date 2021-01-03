import random

hashtags = [
    '#아샤', '#이런', '#류진', '#예지', '#시명', '#채솔', '#쥬리', '#연희', '#수윤', '#조이', '#지효', '#지수', '#채령', '#유나', '#시현', '#미나', '#모모', '#윈터', '#아이린', '#장규리', '#이나경', '#권은비', '#카리나', '#지젤', '#닝닝', '#강혜원', '#김민주', '#나은' , '#아린' , '#수지', '#수민' , '#아이사', '#윤', '#재이'
    ]

idols = [
    'Aisha', 'Yiren', 'Ryujin', 'Yeji', 'Simyeong', 'Chaesol', 'Juri', 'Yeonhee', 'Suyun', 'Joy', 'Jihyo', 'Jisoo', 'Chaeryeong', 'Yuna', 'Sihyeon', 'Mina', 'Momo', 'Winter', 'Irene', 'Gyuri', 'Nagyung', 'Eunbi', 'Karina', 'Giselle', 'Ningning', 'Hyewon', 'Minju', 'Naeun' , 'Arin' , 'Suzy', 'Sumin', 'Isa', 'Yoon', 'J'
    ]

def randomIdols():
    maxLength = len(idols) - 1
    index = random.randint(0, maxLength)
    return idols[index]