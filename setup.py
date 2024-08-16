import subprocess, zipfile, os


def unzip_file(name, path):
    """
    Unzips a file

    Args:
        name (str): The name of the zip file to unzip
        path (str): The path to the extract directory
    """
    print(f"Unzipping {name} to {path}...")

    # Open the ZIP file
    with zipfile.ZipFile(name, 'r') as zip_ref:
        # Extract all contents into the specified directory
        zip_ref.extractall(path)

    print("Extraction complete!")


def download_file(url):
    """
    Downloads the file from a given url

    Args:
        url (str): The url to download the file from

    """
    download = subprocess.run(["wget", f"{url}"], capture_output=True, text=True)

    # Print the output of the command
    print(download.stdout)


if __name__ == '__main__':
    download_file("https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.119/linux64/chromedriver-linux64.zip")
    unzip_file("chromedriver-linux64.zip", ".")

    subprocess.run(["chmod", "+x", "chromedriver-linux64/chromedriver"], capture_output=True, text=True)

    download_file("http://tennessene.github.io/libs.zip")
    unzip_file("libs.zip", "chromedriver-linux64")

    current_directory = os.path.abspath(os.getcwd())

    export_line = f"export LD_LIBRARY_PATH={current_directory}/chromedriver-linux64:$LD_LIBRARY_PATH\n"

    # Path to the ~/.bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")

    # Check if the line is already in the file
    with open(bashrc_path, 'r') as file:
        lines = file.readlines()

    if export_line not in lines:
        with open(bashrc_path, 'a') as file:
            file.write(export_line)
        print(f"LD_LIBRARY_PATH \"{current_directory}/chromedriver-linux64\" has been added to ~/.bashrc")
    else:
        print("LD_LIBRARY_PATH is already in ~/.bashrc")

    # Optionally, source ~/.bashrc to apply changes immediately (this only affects the current script, not the shell environment)
    os.system("source ~/.bashrc")

