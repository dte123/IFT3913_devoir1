import csv
import math
import os


def clean_path(path_: str):
    path_ = path_.strip().replace("\\", "/")
    return str(os.path.abspath(path_))


# JLS
def jls(folder_path=""):
    work_dir = os.path.abspath(folder_path)
    filelist = []

    for root, _, files in os.walk(work_dir):
        for file in files:
            if file.endswith(".java"):
                package = str(root).split("java")[1].replace(str(os.sep), ".")[1:]
                class_name = (
                    str(os.path.join(root, file)).split(str(os.sep))[-1].split(".")[0]
                )
                file_ = {
                    "filepath": os.path.abspath(os.path.join(root, file)),
                    "package": package,
                    "class_name": class_name,
                }
                filelist.append(file_)
    return filelist


def write_to_csv(folder_path: str):
    csv_output = jls(folder_path)
    keys = csv_output[0].keys()

    with open("jls_output.csv", "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(csv_output)


def _jls():
    # C:\Users\Admin\Documents\Assignment\IFT3913_devoir1\jfreechart\src\main\java
    file_input = input("Input the absolute folder path: ")
    file_input = clean_path(file_input)
    if not os.path.isdir(file_input):
        print("Input is not a folder!!! A folder is required")
        exit(1)
    write_to_csv(file_input)
    print("CSV Written successfully to the current working directory")


########### END of JLS

# nvloc
def nvloc(file_name: str):
    if file_name is None:
        return
    if not file_name.endswith(".java"):
        print("Only Java Files are processed")
        return

    file_length = 0
    file_name = os.path.abspath(file_name)

    with open(file_name, "r") as fp:
        for _, line in enumerate(fp):
            li = str(line).strip()
            if li == "" or li.startswith("*") or li.startswith("/"):
                continue
            else:
                file_length += 1

    return file_length


def _nvloc():
    # C:\Users\Admin\Documents\Assignment\IFT3913_devoir1\jfreechart\src\main\java\org\jfree\chart\annotations\CategoryPointerAnnotation.java
    file_input = input("Input the absolute file path: ")
    file_input = clean_path(file_input)
    if not os.path.isfile(file_input):
        print("Input is not a file!!! A file is required")
        exit(1)
    print(f"The nvloc value for file located at '{file_input} is {nvloc(file_input)}")


############# End of NVLOC
# LCSEC


def read_csv(file_path):
    with open(file_path) as f:
        a = [
            {k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)
        ]
    return a


def lcsec(folder_name: str, csv_input_file: str):
    if not folder_name:
        return "Folder name is required"

    if not csv_input_file:
        return "CSV file is required"

    csv_input = read_csv(str(os.path.abspath(csv_input_file)))

    list_classes = [obj["class_name"] for obj in csv_input]

    for obj in csv_input:
        obj["csec"] = count_usages(obj["filepath"], list_classes)

    return csv_input


def count_usages(file_name: str, classes: list | None):
    """
    This function counts on the number of classes being used in a filename
    """
    file_name = os.path.abspath(file_name)
    if file_name is None:
        return
    if not file_name.endswith(".java"):
        print("Only Java Files are processed")
        return
    stringed = read_file_to_string(file_name)
    count = 0

    current_class_name = file_name.split(str(os.sep))[-1].split(".")[0]

    for class_ in classes:
        if class_ == current_class_name:
            continue
        class_ = f" {class_}"
        if class_ in stringed:
            count += 1
    return count


def read_file_to_string(filename):
    """
    This function reads a file into a string
    """
    file_string = ""
    for line in open(filename):
        li = line.strip()
        if li.startswith("/") or li.startswith("*"):
            continue
        else:
            file_string += li + "\n"
    return file_string


def _lcsec():
    file_input = input("Input the absolute folder path for Java Source Code: ")
    file_input = clean_path(file_input)

    if not os.path.isdir(file_input):
        print("Java Source Code Input is not a folder!!! A folder is required")
        exit(1)

    csv_file_input = input("Input the absolute folder path for CSV File: ")
    csv_file_input = clean_path(csv_file_input)

    if not os.path.isfile(csv_file_input):
        print("CSV File Input is not a file!!! A file is required")
        exit(1)

    print("=================LCSEC Output=========================")
    output = sorted(
        lcsec(file_input, csv_file_input), key=lambda d: d["csec"], reverse=True
    )
    for item in output:
        print(
            f"{item['filepath']}, {item['package']}, {item['class_name']}, {item['csec']}"
        )


############# END of LCSEC
# EGON
def egon(folder_name: str, threshold: float):
    folder_name = os.path.abspath(folder_name)
    # Run JLS to generate CSV
    jls(folder_name)
    output = lcsec(folder_name, os.path.join(os.getcwd(), "jls_output.csv"))

    for obj in output:
        obj["nvloc"] = nvloc(obj["filepath"])
    top = threshold / 100 * len(output)

    # Filter the output to the threshold of CSEC
    sorted_by_nvloc = sorted(output, key=lambda d: d["nvloc"], reverse=True)
    sorted_by_csec = sorted(sorted_by_nvloc, key=lambda d: d["csec"], reverse=True)[
        : math.ceil(top)
    ]
    sorted_by_nvloc = sorted_by_nvloc[: math.ceil(top)]

    suspected_classes = list()

    for obj in output:
        if obj in sorted_by_csec and obj in sorted_by_nvloc:
            suspected_classes.append(obj)
    return sorted(suspected_classes, key=lambda d: d["csec"], reverse=True)


def _egon():
    file_input = input("Input the absolute folder path for Java Source Code: ")
    file_input = clean_path(file_input)

    if not os.path.isdir(file_input):
        print("Java Source Code Input is not a folder!!! A folder is required")
        exit(1)

    threshhold = input("Enter a threshold 1-100 (int): ")

    suspected_classes = egon(file_input, float(threshhold))

    for suspected_class in sorted(
        suspected_classes, key=lambda d: d["csec"], reverse=True
    ):
        print(
            f"{os.path.abspath(suspected_class['filepath'])}, {suspected_class['package']}, {suspected_class['class_name']}, {suspected_class['csec']}, {suspected_class['nvloc']}"
        )


def run_jfreecharts():
    threshhold = input("Enter a threshold 1-100 (int): ")

    suspected_classes = egon("./jfreechart/src/main/java", float(threshhold))

    for suspected_class in sorted(
        suspected_classes, key=lambda d: d["csec"], reverse=True
    ):
        print(
            f"{os.path.abspath(suspected_class['filepath'])}, {suspected_class['package']}, {suspected_class['class_name']}, {suspected_class['csec']}, {suspected_class['nvloc']}"
        )


def ask_for_an_action():
    choice = input(
        "Select an Action to Run: \n1. Part 0 - jls\n2. Part 1 - nvloc\n3. Part 2 - lcsec\n4. Part 3 - egon\n 5.Part 4 - Run tool on jfreechart\n6.Exit\n"
    )
    return int(choice)


if __name__ == "__main__":
    choice = ask_for_an_action()
    if int(choice) == 1:
        _jls()
    elif int(choice) == 2:
        _nvloc()
    elif int(choice) == 3:
        _lcsec()
    elif int(choice) == 4:
        _egon()
    elif int(choice) == 5:
        pass
    elif int(choice) == 6:
        exit(1)
    else:
        print("Invalid Input, Try again...\n")
    exit()

    # test_jls()
    # test_nvloc()
    # test_lcsec()
    # test_egon()
