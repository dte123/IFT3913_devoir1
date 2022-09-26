import csv
import os


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


def test_lcsec():
    output = sorted(
        lcsec("./jfreechart/src/main/java", "./jls/jls_output.csv"),
        key=lambda d: d["csec"],
        reverse=True,
    )
    for item in output:
        print(
            f"{item['filepath']}, {item['package']}, {item['class_name']}, {item['csec']}"
        )


if __name__ == "__main__":
    test_lcsec()
