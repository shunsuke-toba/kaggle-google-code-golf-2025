import os, shutil
import json
from tqdm import tqdm
for i in tqdm(range(1, 401)):
    json_data = json.load(open(f"{i:03d}/0_input.json"))
    os.makedirs(f"{i:03d}/testcases/", exist_ok=True)
    for key in ["train", "test", "arc-gen"]:
        id = 0
        for case in json_data[key]:
            input_text = ""
            output_text = ""
            for row in case["input"]:
                for num in row:
                    input_text += f"{num}"
                input_text += "\n"
            for row in case["output"]:
                for num in row:
                    output_text += f"{num}"
                output_text += "\n"
            with open(f"{i:03d}/testcases/{key}_{id}.txt", "w") as f:
                f.write(input_text)
                f.write("\n")
                f.write(output_text)
            id += 1