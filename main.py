path_to_file = "books/frankenstein.txt"

def count_words(text):
  word_count = len(text.split())
  print(f"{word_count} words found in the document")

def count_letters(text):
    letter_dict = {}
    for letter in text.lower():
      if letter in letter_dict:
        letter_dict[letter] += 1
      else:
        letter_dict[letter] = 1

    letter_list = []
    for letter in letter_dict:
      if letter.isalpha():
        letter_list.append(f"{letter_dict[letter]};The '{letter}' character was found {letter_dict[letter]} times")
    letter_list.sort(key=lambda x: int(x[:x.index(";")]), reverse=True)
    for letter_data in letter_list:
      print(letter_data[letter_data.index(";") + 1:])

print(f"--- Begin report of {path_to_file} ---")
with open(path_to_file) as f:
    file_contents = f.read()

    count_words(file_contents)
    print()
    count_letters(file_contents)
print("--- End report ---")
