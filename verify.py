import copy
import importlib.util
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=SyntaxWarning)

libraries = ["collections", "itertools", "math", "operator", "re", "string", "struct"]


def verify_program(task_num, examples, task_path, verbose=True):
    task_name = "task_with_imports"
    spec = importlib.util.spec_from_file_location(task_name, task_path)
    if spec is None:
        print("Error: Unable to import task.py.")
        return
    module = sys.modules[task_name] = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "p"):
        print("Error: Unable to locate function p() in task.py.")
        return
    program = getattr(module, "p")
    if not callable(program):
        print("Error: Function p() in task.py is not callable.")
        return

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
            except Exception as e:
                if verbose:
                    print(f"Error processing example: {e}")
                wrong += 1
        return right, wrong, expected

    arc_agi_right, arc_agi_wrong, arc_agi_expected = verify(
        examples["train"] + examples["test"]
    )
    arc_gen_right, arc_gen_wrong, arc_gen_expected = verify(examples["arc-gen"])
    if verbose:
        print(f"Results on ARC-AGI exaples: {arc_agi_right} pass, {arc_agi_wrong} fail")
        print(f"Results on ARC-GEN exaples: {arc_gen_right} pass, {arc_gen_wrong} fail")
        print()
    if arc_agi_wrong + arc_gen_wrong == 0:
        task_length = os.path.getsize(task_path)
        if verbose:
            print("Your code IS READY for submission!")
            print("Its length appears to be " + str(task_length) + " bytes.")
            print("Next steps:")
            print(
                " * Copy it into a file named task{:03d}.py on your local machine.".format(
                    task_num
                )
            )
            print(" * Create a zip file containing that program along with all others.")
            print(
                " * Submit that zip file to the Kaggle competition so that it can be officially scored."
            )

        solution = open(task_path).read()
        score = max([0.1, 2500 - len(solution.encode("utf-8"))])
        return score
    else:
        expected = arc_agi_expected if arc_agi_expected else arc_gen_expected
        if not expected:
            return 0
        if not verbose:
            return 0
        actual = {}
        actual["input"] = expected["input"]
        actual["output"] = program(copy.deepcopy(expected["input"]))
        print("Your code IS NOT ready for submission.")
        print(
            "The expected result is shown in green; your actual result is shown in red."
        )
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
    code_type = str(sys.argv[2]) if len(sys.argv) > 2 else "sub"
    examples_path = f"{task_num:03d}/0_input.json"
    with open(examples_path, "r") as file:
        examples = json.load(file)
    code_path = (
        f"{task_num:03d}/3_submission.py"
        if code_type == "sub"
        else f"{task_num:03d}/2_plain_code.py"
    )
    verify_program(task_num, examples, code_path)
