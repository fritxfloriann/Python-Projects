languages = ["English", "Mandarin", "German", "Spanish"]

print(languages[0])

print(languages[1])

programming_languages = ["Python", "C#", "C"]

print(programming_languages[0])

programming_languages.append("JavaScript")

print(programming_languages)

programming_languages.append("Assembly")

programming_languages.append("C++")

print(programming_languages)

programming_languages = ["Python", "C#", "C", "JavaScript", "Assembly", "C++"]

programming_languages.remove("C")

print(programming_languages)

programming_languages = ["Python", "C#", "JavaScript", "Assembly", "C++"]

programming_languages.remove("C#")

print(programming_languages)

languages = ["English", "Mandarin", "German", "Spanish"]

print(len(languages))

languages = ["English", "Mandarin", "German", "Spanish"]

known_languages = input(
    "Enter the languages you know, separated by commas: "
).split(",")

known_languages = [lang.strip().title() for lang in known_languages if lang.strip()]

for language in known_languages:
    if language not in languages:
        print(f"{language} isn't in the list!")

if len(known_languages) >= 3:
    print("You are multilingual.")

elif len(known_languages) == 2:
    print("You are bilingual.")

else:
    print("You are monolingual.")

languages = ["English", "Mandarin", "German", "Spanish"]

for language in languages:
    print(language)

programming_languages = ["Python", "C#", "C", "JavaScript", "Assembly", "C++"]

for programming_language in programming_languages:
    print(programming_language)

print(languages[1])
