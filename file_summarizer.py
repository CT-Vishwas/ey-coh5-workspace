import string
from pathlib import Path
import os
from datetime import datetime as dt

SUMMARY_LOG = "summary.log"
VOWELS = "aeiouAEIOU"

def calculate(file_path, summary={}):
    count_digits = 0
    count_vowels = 0
    count_puns = 0
    with open(file_path) as fh:
        data = fh.read()
        summary["Number of Characters"] = len(data)

        for chr in data:
            if chr in VOWELS:
                count_vowels += 1
            if chr in string.punctuation:
                count_puns += 1
            if chr in string.digits:
                count_digits += 1

    summary["Number of Digits"] = count_digits
    summary["Number of Vowels"] = count_vowels
    summary["Number of Punctuations"] = count_puns

    with open(file_path) as fh:
        data = fh.readlines()
        summary["Number of Lines"] = len(data)
        count_words = 0
        for line in data:
            words = line.split()
            count_words += len(words)
        summary["Number of Words"] = count_words 

    return summary

def main(file_path):
    # Extract the filename
    p = Path(file_path)
    fname = os.path.basename(file_path)
    summary = {
        "File Name": "",
        "Time Stamp": "Date",
        "Number of Characters": 0,
        "Number of Lines": 0,
        "Number of Words": 0,
        "Number of Digits": 0,
        "Number of Vowels": 0,
        "Number of Punctuations": 0,
    }

    # Calculate
    summary = calculate(file_path, summary)
    summary["File Name"] = fname
    summary["Time Stamp"] = dt.now().isoformat()
    
    # Write to a File
    with open(SUMMARY_LOG, "a+") as fh:
        fh.write(f"Summary of {summary["File Name"]} at {summary["Time Stamp"]}\n")
        fh.write("-"*70+"\n")
        for k,v in summary.items():
            if k != "File Name" or k != "Time Stamp":
                fh.write(k+"\t"+str(v)+"\n")
        fh.write("-"*70+"\n")

if __name__ == '__main__':
    file_path = input("Enter File path: ")
    main(file_path)