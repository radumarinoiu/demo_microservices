import json

# data = {}
# data['people'] = []
# data['people'].append({
#     'name' : 'Scott',
#     'website' : 'stackabuse',
#     'type' : 'commercial'
# })
# data['people'].append({
#     'name' : 'Larry',
#     'website' : 'canadiansextips',
#     'type' : 'non-profit'
# })

# with open('database.json', 'w') as outfile:
#     json.dump(data, outfile)

global STUDENT_LIST

STUDENT_LIST = []

with open('database.json', 'r') as json_file:
    STUDENT_LIST = json.load(json_file)
    STUDENT_LIST['students'].sort(key = lambda x: x['average'])

input = open('input.txt', 'r')

if(input.read() == 'GET_STUDENTS'):
    for student in STUDENT_LIST['students']:
        print('')
        print('Student ' + student['name'] + ' with average ' + student['average'])
else:
    print('Wrong command ')
