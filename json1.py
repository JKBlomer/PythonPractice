import json

people_string = '''
{
    "people": [
        {
            "name": "Jessica Blomer",
            "phone": "333-333-3333",
            "emails": ["jess@company.com", "jessica@email.com"],
            "has_license": "false"
        
        },
        {
            "name": "Jane Jarlson",
            "phone": "444-444-4444",
            "emails": null,
            "has_license": "true"
        }
    ]
}
'''


data = json.loads(people_string)
# print(type(data["people"]))
# print(type(data["people"][1]))

# for person in data["people"]:
    # print(person)


# new_data = json.dumps(data)
#if you want your string indented, add indent parameter
new_data = json.dumps(data, indent=1)
print(type(new_data))
print(new_data)