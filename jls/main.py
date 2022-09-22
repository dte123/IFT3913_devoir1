import csv
import os


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


def test_jls():
    write_to_csv("../jfreechart/src/main/java")


if __name__ == "__main__":
    test_jls()
