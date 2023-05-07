import os


directory = "/home/uit-lim/vspython/directory/Spanish mackerel/new_txt"

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as f:
        text = f.read()
    text = text.replace(old_text, new_text)
    with open(file_path, 'w') as f:
        f.write(text)

origin = "2"
change = "3"

file_paths = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")]
for file_path in file_paths:
    replace_text_in_file(file_path, origin, change)

print("end")
