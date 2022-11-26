from re import match, sub, DOTALL
import os


def insert_copyright(file, cp):
    with open(file, "r+") as f:
        file_loaded = f.read()
        result = sub(
            r"# BEGIN COPYRIGHT(?s).*# END COPYRIGHT",
            "# BEGIN COPYRIGHT\n# " + cp + "# END COPYRIGHT",
            file_loaded,
            flags=DOTALL,
        )
    with open(file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    with open("info.txt", "r") as f:
        copyright_loaded = f.read()
    insert_copyright("pythonesque.py", copyright_loaded)


# "# BEGIN COPYRIGHT(?s)(.*)# END COPYRIGHT",
