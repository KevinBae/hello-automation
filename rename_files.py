import os, sys, time

def rename_files(prefix="renamed_", folder="."):
    for name in os.listdir(folder):
        p = os.path.join(folder, name)
        if os.path.isfile(p) and not name.startswith(prefix):
            new = prefix + name
            os.rename(p, os.path.join(folder, new))
            print(f"{name} -> {new}")

def rename_with_timestamp(folder="."):
    ts = time.strftime("%Y%m%d-%H%M%S")
    for name in os.listdir(folder):
        p = os.path.join(folder, name)
        if os.path.isfile(p):
            new = f"{ts}-{name}"
            os.rename(p, os.path.join(folder, new))
            print(f"{name} -> {new}")

if __name__ == "__main__":
    # usage:
    #   python rename_files.py prefix [folder]
    #   python rename_files.py ts [folder]
    arg1 = sys.argv[1] if len(sys.argv) > 1 else "renamed_"
    folder = sys.argv[2] if len(sys.argv) > 2 else "."
    if arg1 == "ts":
        rename_with_timestamp(folder)
    else:
        rename_files(prefix=arg1, folder=folder)
