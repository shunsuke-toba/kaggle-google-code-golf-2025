import os, json
from verify import verify_program

score_sum = 0
for i in range(1, 401):
    examples_path = f"{i:03d}/0_input.json"
    with open(examples_path, "r") as file:
        examples = json.load(file)
    code_path = f"{i:03d}/3_submission.py"
    with open(code_path, 'r') as f:
        content = f.read()
    if len(content) <= 1:
        print(f"{i:03d} : unsolved")
        continue
    try:
        score = verify_program(i, examples, code_path, verbose=False)
        if score > 0:
            print(f"{i:03d} : {score}")
            score_sum += score
        else:
            print(f"{i:03d} : implemented but not correct")
    except Exception as e:
        print(f"{i:03d} : error occurred - {str(e)}")
        score = 0

print(f"Total Score: {score_sum}")