import os

# strip the last part of the filename
def strip_notion_filecode(files_dir: str, output_dir: str):
    for file in os.listdir(files_dir):
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(files_dir, file)
        

def construct_md_file_paths(files_dir: str):
    for file in os.listdir(files_dir):
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(files_dir, file)
        yield file_path