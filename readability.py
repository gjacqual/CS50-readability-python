from cs50 import get_string
import re


def main():
    # ask user text
    text = get_string("Text: ")

    # count letters
    letters = len([i for i in text if i.isalpha()])

    # count words
    words = len(text.split())

    # count sentences. I found the idea to use re module here https://coderoad.ru/15228054/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B5-%D0%B2-python
    # If the end of the string matches the pattern,
    # the last element will be an empty string
    sntnc = len(re.split('[.!?]', text)) - 1

    # calculate the average number of letters per 100 words
    mid_l = letters * 100 / words

    # calculate the average number of sentences per 100 words
    mid_s = sntnc * 100 / words

    # find coleman-Liau index
    index = 0.0588 * mid_l - 0.296 * mid_s - 15.8

    if index < 1:
        # output in the case when the score is less than 1
        print("Before Grade 1")
    elif index >= 16:
        # output in the case when the score is greater than or equal to 16
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")


main()