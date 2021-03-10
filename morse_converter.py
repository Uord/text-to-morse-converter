import pandas as pd

morse_code = pd.read_csv('morse.csv', header=None)
morse_code_dict = {row[0]: row[1] for (
    index, row) in morse_code.iterrows()}


def convert_text(text):
    """Convert text to morse code"""
    converted_text = ''
    for element in text.upper():
        if element in morse_code_dict:
            converted_text += morse_code_dict[element]
            converted_text += ' '
        elif element == ' ':
            converted_text += '  '
        elif element in ['.', ',', '!', '?', ';']:
            converted_text += '      '
        else:
            converted_text += '   '
    return print(converted_text)


text = input('Text you want to convert to morse code: ')

convert_text(text)
