# this script will generate mod.rs files that let rust-analyzer work 
# without `rust-project.json` on the rustlings examples.

import os
import glob

for folder in glob.glob("exercises/*"):
    if not os.path.isdir(folder):
        continue
    with open(os.path.join(folder, "mod.rs"), "w") as f:
        for file in glob.glob(os.path.join(folder, "*.rs")):
            if not os.path.isfile(file) or os.path.basename(file) == "mod.rs":
                continue
            filename = os.path.splitext(os.path.basename(file))[0]
            f.write(f"mod r#{filename};\n")

# write the base module
with open("exercises/mod.rs", "w") as f:
    f.write("#![allow(dead_code)]\n")
    for folder in glob.glob("exercises/*"):
        if os.path.isdir(folder):
            foldername = os.path.basename(folder)
            f.write(f"mod r#{foldername};\n")

# make sure cargo.toml has the lib defined:
lib = """
[lib]
name = "exercises"
path = "exercises/mod.rs"
"""

with open("Cargo.toml", "r") as f:
    if 'name = "exercises"' not in f.read():
        with open("Cargo.toml", "a") as f:
            f.write(lib)
