from pathlib import Path

def list_csv_files(folder):
    return list(Path(folder).glob("*.csv"))

if __name__ == "__main__":
    files = list_csv_files("./data")
    for file in files:
        print(file)
