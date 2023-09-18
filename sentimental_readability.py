import cs50


text = cs50.get_string("Text: ")
letters = len([char for char in text if char.isalpha()])
words = len(text.split())
sentences = len([char for char in text if char == "!" or char == "." or char == "?"])

avg_letters = letters / words * 100
avg_sentences = sentences / words * 100
grade_index = round(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8)

if grade_index < 1:
    print("Before Grade 1")
elif grade_index > 16:
    print("Grade 16+")
else:
    print(f"Grade {grade_index}")
