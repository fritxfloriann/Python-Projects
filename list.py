
# Doing Lists in Python

# Instead of the traditional method of doing variables, we will be making it into one list.

languages = ["English", "Mandarin", "German", "Spanish"]

# This is much cleaner than typing each languages in separate variables.

# And Python uses indexing for each variable. Remember, it should start at zero.

print(languages[0])

# This should print the first variable, which is English.

print(languages[1])

# With the second print, this should say Mandarin.

# Now let's try adding items in a list, or should I say, appending.

programming_languages = ["Python", "C#", "C"]

print(programming_languages[0])

# This should say Python, but what if we want to add another programming language? We will use append to add variables in the list,

programming_languages.append("JavaScript")

print(programming_languages)

# The new variable, "JavaScript", should be added to the list of variables.

# You also keep adding variables to the list.

programming_languages.append("Assembly")

programming_languages.append("C++")

print(programming_languages)

# You can continuously add variables into a list by appending them, but what about removing them?

# Now what about removing variables from a list? Let's focus on the removal of variables in a list.

programming_languages = ["Python", "C#", "C", "JavaScript", "Assembly", "C++"]

# The list contains a lot of variables. Let's remove one.

programming_languages.remove("C")

print(programming_languages)

programming_languages = ["Python", "C#", "JavaScript", "Assembly", "C++"]

programming_languages.remove("C#")

print(programming_languages)

# Remember, the .remove command only removes one variable.

# And now, let's use the len() command. We will be using languages again.

languages = ["English", "Mandarin", "German", "Spanish"]

print(len(languages))

# It should output the quantity of the list. Now let's incoperate if and input.

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

# This is how you can use functions to make the list interactable.

# You can also use loops for structuring and looping the list.

languages = ["English", "Mandarin", "German", "Spanish"]

for language in languages:
    print(language)

# This will print the list of languages in a list format.

# Trying the Programming Languages variables next, it does the same results:

programming_languages = ["Python", "C#", "C", "JavaScript", "Assembly", "C++"]

for programming_language in programming_languages:
    print(programming_language)

# You can pick from the list by doing the following Python:

print(languages[1])

# It will print the second variable in the list, "C#".