username = "vinith-1311"
repo = "vinith-python-scripts"
file_path = "hello.py"  # The path of the file in your repository
branch = "main"  # Default branch is usually 'main' or 'master'

url = f"https://raw.githubusercontent.com/{vinith-1311}/{vinith-python-scripts}/{main}/{hello.py}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues
    print("Fetched Script Content:")
    print(hello.py)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the script: {e}")
