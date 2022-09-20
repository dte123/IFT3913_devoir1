from egon.main import egon
from jls.main import jls
from nvloc.main import nvloc
from lcsec.main import lcsec

def test_jls():
    output = jls("./jfreechart/src/main/java")
    for item in output:
        print(f"{item['filepath']}, {item['package']}, {item['class_name']}")


def test_nvloc():
    print(nvloc(file_name="./jfreechart/src/main/java/org/jfree/data/xy/YWithXInterval.java"))

def test_lcsec():
    output = sorted(lcsec('./jfreechart/src/main/java'),key=lambda d: d['csec'], reverse=True)
    for item in output:
        print(f"{item['filepath']}, {item['package']}, {item['class_name']}, {item['csec']}")


def test_egon():
    print(egon('./jfreechart/src/main/java', 5.0))

if __name__ == "__main__":
    # test_jls()
    # test_nvloc()
    test_lcsec()
    # test_egon()