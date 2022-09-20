from jls.main import jls
import os


def lcsec(folder_name="", csv_input=None):
    if not folder_name:
        return "Folder name is required"

    if not csv_input:
        csv_input = jls(folder_name)
    else:
        if csv_input != jls(folder_name):
            print("CSV Input doesn't match with the expected generation... \nGenerating New One")

    list_classes = [obj['class_name'] for obj in csv_input]
    for obj in csv_input:
        obj['csec'] = count_usages(obj['filepath'], list_classes)

    return csv_input


def count_usages(file_name: str, classes: list | None):
    """
    This function counts on the number of classes being used in a filename
    """
    file_name = os.path.abspath(file_name)
    if file_name is None:
        return
    if not file_name.endswith('.java'):
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
            file_string += li +"\n"
    return file_string