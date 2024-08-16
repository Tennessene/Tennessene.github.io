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

    delete_file(name)


def download_file(url):
    """
    Downloads the file from a given url

    Args:
        url (str): The url to download the file from
    """
    download = subprocess.run(["wget", f"{url}"], capture_output=True, text=True)

    # Print the output of the command
    print(download.stdout)


def delete_file(path):
    """
        Downloads the file from a given url

        Args:
            path (str): The path to the file to delete
        """
    # Check if the file exists before attempting to delete
    if os.path.exists(path):
        os.remove(path)
        print(f"File {path} has been deleted.")
    else:
        print(f"The file {path} does not exist.")


def write_to_bashrc(line):
    """
        Downloads the file from a given url

        Args:
            line (str): The line to write
        """
    # Path to the ~/.bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")

    # Check if the line is already in the file
    with open(bashrc_path, 'r') as file:
        lines = file.readlines()

    if line not in lines:
        with open(bashrc_path, 'a') as file:
            file.write(line)
        print(f"{line} has been added to ~/.bashrc")
    else:
        print("That is already in ~/.bashrc")


if __name__ == '__main__':
    download_file("https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.119/linux64/chrome-linux64.zip")
    unzip_file("chrome-linux64.zip", ".")

    download_file("http://tennessene.github.io/chrome-libs.zip")
    unzip_file("chrome-libs.zip", "libs")

    subprocess.run(["chmod", "+x", "chrome-linux64/chrome"], capture_output=True, text=True)

    download_file("https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.119/linux64/chromedriver-linux64.zip")
    unzip_file("chromedriver-linux64.zip", ".")

    download_file("http://tennessene.github.io/driver-libs.zip")
    unzip_file("driver-libs.zip", "libs")

    subprocess.run(["chmod", "+x", "chromedriver-linux64/chromedriver"], capture_output=True, text=True)

    current_directory = os.path.abspath(os.getcwd())

    library_line = f"export LD_LIBRARY_PATH={current_directory}/libs:$LD_LIBRARY_PATH\n"

    write_to_bashrc(library_line)

    # Optionally, source ~/.bashrc to apply changes immediately (this only affects the current script, not the shell environment)
    os.system("source ~/.bashrc")

