import json

count = 0
ids = {}
with open('data.txt', encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        print(line)
        ids[line] = False
    while True:
        student_id = input("Please scan: ")[:-1]
        print("id:", student_id)
        if student_id == "stop":
            break
        if student_id in ids.keys():
            if ids[student_id] == False:
                print("Success")
                ids[student_id] = True
                count += 1
            else:
                print("Fail") # already scanned
        else:
            print("Not in the student list")
        with open('result.json', 'w') as file:
            file.write(json.dumps(ids))
print(count)
