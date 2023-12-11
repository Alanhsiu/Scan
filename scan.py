import json
import time

count = 0
ids = {}
with open('data.txt', encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        # print(line)
        ids[line] = False
    while True:
        student_id = input("Please scan: ")[:-1]
        # print("id:", student_id)
        if student_id == "stop":
            break
        if student_id in ids.keys():
            if ids[student_id] == False:
                count += 1
                # print current time
                print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "Success", count)
                ids[student_id] = True
                with open('record_time.txt', 'a') as file:
                    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + student_id + "\n")
            else:
                # already scanned
                print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "Fail")
        else:
            print("Not in the student list")
        with open('result.json', 'w') as file:
            file.write(json.dumps(ids))
print(count)
