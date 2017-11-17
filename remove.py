import glob, os
for f in glob.glob("*.txt"):
    os.remove(f)
