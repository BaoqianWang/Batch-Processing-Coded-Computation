import json



with open('parameters_configurations.json') as f:
    data=json.load(f)

print(data['host_goal'])
