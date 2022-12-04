def _02a():
    d = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    outcome = {
        'A X': 3,
        'A Y': 6,
        'A Z': 0,
        'B X': 0,
        'B Y': 3,
        'B Z': 6,
        'C X': 6,
        'C Y': 0,
        'C Z': 3,
    }
    outcome2 = {
        'lose': [
            'A Z',
            'B X',
            'C Y',
        ],
        'draw':[
            'A X',
            'B Y',
            'C Z',
        ],
        'win': [
            'A Y',
            'B Z',
            'C X',
        ]
    }

    data = open("data/day2").read().splitlines()
    
    player = 0
    choice = ''
    for event in data:
        event_robot, event_player = tuple(event.split(" "))
        if event_player == 'X':
            for e in outcome2['lose']:
                if event_robot in e:
                    out = outcome[e]
                    choice = e.split(" ")[-1]
        if event_player == 'Y':
            for e in outcome2['draw']:
                if event_robot in e:
                    out = outcome[e]
                    choice = e.split(" ")[-1]
        if event_player == 'Z':
            for e in outcome2['win']:
                if event_robot in e:
                    out = outcome[e]
                    choice = e.split(" ")[-1]
            
        player += out + d[choice]
    
    print(player)

_02a()