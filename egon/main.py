import math
import os
from jls.main import jls
from lcsec.main import lcsec
from nvloc.main import nvloc


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


def test_egon():
    print(egon("./jfreechart/src/main/java", 5.0))


if __name__ == "__main__":
    test_egon()
