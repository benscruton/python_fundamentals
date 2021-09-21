users = {
    "Students": [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    "Instructors": [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

for k, v in users.items():
    print(k)
    for i in range(len(v)):
        first_name = v[i]["first_name"].upper()
        last_name = v[i]["last_name"].upper()
        num_chars = len(first_name) + len(last_name)
        print(f"{i+1} - {first_name} {last_name} - {num_chars}")

