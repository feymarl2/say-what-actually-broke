import os

LINE = "Error 500: Otak server meleleh karena terlalu lama memikirkan alasan kenapa tombol 'Submit' tiba-tiba hilang."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
