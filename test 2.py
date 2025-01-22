import json
a={
    "cmotry": "cuda"
    }
b=json.dumps(a)
with open("здравствуй.json", "w") as my_file:
    my_file.write(b)
