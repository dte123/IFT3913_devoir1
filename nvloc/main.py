import os


def nvloc(file_name: str):
    if file_name is None:
        return
    if not file_name.endswith('.java'):
        print("Only Java Files are processed")
        return

    file_length = 0
    file_name = os.path.abspath(file_name)

    with open(file_name, 'r') as fp:
        for _, line in enumerate(fp):
            li = str(line).strip()
            if li == "" or li.startswith("*") or li.startswith("/"):
                continue
            else:
                file_length += 1

    return file_length