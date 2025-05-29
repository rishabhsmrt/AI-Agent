import shutil

def delete_folder_with_contents(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and all its contents have been deleted.")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")

# Example usage
delete_folder_with_contents('../.logs/')