students = [{"name":"Alex", "gpa":3.2}, {"name":"Karl", "gpa": 2.85},  {"name":"Lulu", "gpa":3.6}, {"name":"Andrea", "gpa": 1.4},  {"name":"Malika", "gpa":3.3}, {"name":"Mike", "gpa": 1.7},  {"name":"Peter", "gpa": 2.4}, {"name":"Noel", "gpa":1.8},  {"name":"Mon", "gpa":1.4}, {"name":"Alice", "gpa":3.8},  {"name":"Ben", "gpa":2.9}, {"name":"Saira", "gpa":1.2}] 
for studs in students:
    if studs['gpa'] >= 2.85:
        print(f"{studs['name']} has a gpa of {studs['gpa']}")
