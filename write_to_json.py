import json
name = 'test'
class_is = 'test class'
race = 'race'


def player_data(player_input):
    data = {}
    data['players'] = []
    data['players'].append({
        'name': player_input,
        'class': player_input,
        'race': player_input
    })
