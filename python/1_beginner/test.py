FAANG = {
    'F': 'Facebook',
    # 'A1': 'Apple',
    # 'A2': 'Amazon',
    'N': 'NEXON', # 잘못 입력했어요!
    'G': 'Google',
}

FAANG.update(N = 'Netflix') # update 하기

print(FAANG) # {'F': 'Facebook', 'N': 'Netflix', 'G': 'Google'}

AA = {
    'A1': 'Apple',
    'A2': 'Amazon',
}

FAANG.update(AA)

print(FAANG) #
