import copy
import importlib.util
import json
import os
import sys

libraries = ["collections", "itertools", "math", "operator", "re", "string",
             "struct"]

def verify_program(task_num, examples, task_path):
  task_name = "task_with_imports"
  module_path = "temp.py"
  with open(task_path, "r") as file:
    file_content = file.read()
    if "import" in file_content:
      print("Error: Imports are not permitted")
      return 0
  with open(module_path, "w") as file:
    for library in libraries:
      file.write(f"from {library} import *\n")
    file.write(file_content)
  spec = importlib.util.spec_from_file_location(task_name, module_path)
  if spec is None:
    print("Error: Unable to import task.py.")
    return 0
  module = sys.modules[task_name] = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  if not hasattr(module, "p"):
    print("Error: Unable to locate function p() in task.py.")
    return 0
  program = getattr(module, "p")
  if not callable(program):
    print("Error: Function p() in task.py is not callable.")
    return 0
  print()
  def verify(example_subset):
    right, wrong, expected = 0, 0, None
    for example in example_subset:
      example_copy = copy.deepcopy(example)
      try:
        if program(example_copy["input"]) == example_copy["output"]:
          right += 1
        else:
          expected = copy.deepcopy(example)
          wrong += 1
      except:
        wrong += 1
    return right, wrong, expected
  arc_agi_right, arc_agi_wrong, arc_agi_expected = verify(examples["train"] + examples["test"])
  arc_gen_right, arc_gen_wrong, arc_gen_expected = verify(examples["arc-gen"])
  print(f"Results on ARC-AGI exaples: {arc_agi_right} pass, {arc_agi_wrong} fail")
  print(f"Results on ARC-GEN exaples: {arc_gen_right} pass, {arc_gen_wrong} fail")
  print()
  os.remove(module_path)  # Clean up the temporary module file
  if arc_agi_wrong + arc_gen_wrong == 0:
    task_length = os.path.getsize(task_path)
    print("Your code IS READY for submission!")
    print("Its length appears to be " + str(task_length) + " bytes.")
    print("Next steps:")
    print(" * Copy it into a file named task{:03d}.py on your local machine.".format(task_num))
    print(" * Create a zip file containing that program along with all others.")
    print(" * Submit that zip file to the Kaggle competition so that it can be officially scored.")

    solution = open(task_path).read()
    score = max([0.1,2500-len(solution.encode('utf-8'))])
    return score
  else:
    print("Your code IS NOT ready for submission.")
    expected = arc_agi_expected if arc_agi_expected else arc_gen_expected
    if not expected: return
    actual = {}
    actual["input"] = expected["input"]
    actual["output"] = program(copy.deepcopy(expected["input"]))
    print("The expected result is shown in green; your actual result is shown in red.")
    print("Input:")
    for row in expected["input"]:
      print(row)
    print("Expected output:")
    for row in expected["output"]:
      print(row)
    print("Your output:")
    for row in actual["output"]:
      print(row)
    return 0
  


if __name__ == "__main__":
  task_num = int(sys.argv[1])
  code_type = str(sys.argv[2]) # "sub" or "plain"
  examples_path = f"{task_num:03d}/0_input.json"
  with open(examples_path, "r") as file:
    examples = json.load(file)
  code_path = f"{task_num:03d}/3_submission.py" if code_type == "sub" else f"{task_num:03d}/2_plain_code.py"
  verify_program(task_num, examples, code_path)