import zipfile

def extract_zip(zip_path, extract_to):
    """Extracts a ZIP file to the specified directory.

    Args:
        zip_path (str): The path to the ZIP file.
        extract_to (str): The directory where files will be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


if __name__ == "__main__":
    print("This is a utility module for extracting ZIP files.")

