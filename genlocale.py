import json
import os
import sys


def updatenested(src_data, dest_data):
    for key, value in src_data.items():
        if isinstance(value, dict):
            dest_data[key] = dest_data.get(key, {})
            updatenested(value, dest_data[key])
        else:
            dest_data.setdefault(key, value)

def copylocale(src_locale, dest_locale):
    with open(src_locale, 'r', encoding='utf-8') as f:
        src_data = json.load(f)

    if os.path.exists(dest_locale):
        with open(dest_locale, 'r', encoding='utf-8') as f:
            dest_data = json.load(f)
    else:
        dest_data = {}

    updatenested(src_data, dest_data)

    with open(dest_locale, 'w', encoding='utf-8') as f:
        json.dump(dest_data, f, indent=4, ensure_ascii=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 genlocale.py <locale such as '<2 alphabets of the country code like 'jp', 'es', etc.>'>")
        return

    src_locale = 'locale/en.json'
    dest_locale = 'locale/' + sys.argv[1] + '.json'

    copylocale(src_locale, dest_locale)

if __name__ == "__main__":
    main()
