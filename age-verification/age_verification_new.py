
# Age Verification using Python

SMALL_NUMBER_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
}
TENS_NUMBER_WORDS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}


def print_dialogue(*messages):
    """Print dialogue lines with a blank line between them."""
    print("\n\n".join(messages))


def parse_number_words(text):
    """Convert standard English number words from zero to one hundred."""
    words = text.lower().replace("-", " ").split()
    words = [word for word in words if word != "and"]

    if words == ["one", "hundred"]:
        return 100
    if len(words) == 3 and words[:2] == ["one", "hundred"]:
        remainder_words = words[2:]
        return 100 + parse_number_words(" ".join(remainder_words))
    if len(words) == 1:
        if words[0] in SMALL_NUMBER_WORDS:
            return SMALL_NUMBER_WORDS[words[0]]
        if words[0] in TENS_NUMBER_WORDS:
            return TENS_NUMBER_WORDS[words[0]]
    if (
        len(words) == 2
        and words[0] in TENS_NUMBER_WORDS
        and words[1] in SMALL_NUMBER_WORDS
        and 1 <= SMALL_NUMBER_WORDS[words[1]] <= 9
    ):
        return TENS_NUMBER_WORDS[words[0]] + SMALL_NUMBER_WORDS[words[1]]
    raise ValueError


def get_age():
    """Ask for an age from zero to one hundred, in digits or words."""
    while True:
        raw_age = input("Enter your age (0-100, digits or words): ").strip()
        try:
            try:
                age = int(raw_age)
            except ValueError:
                age = parse_number_words(raw_age)
            if not 0 <= age <= 100:
                print_dialogue("Age must be between 0 and 100. Please try again.")
                continue
            return age
        except ValueError:
            print_dialogue("Enter a whole-number age using digits or words, from 0 to 100.")


print_dialogue("Welcome to Australian Age Verification System.")
age = get_age()
print()

print_dialogue("Australian Election Age Verification")
if age >= 18:
    print_dialogue(
        "You are eligible to vote.",
        "Remember to register to vote and participate in the democratic process.",
    )
else:
    print_dialogue(
        "You are not eligible to vote.",
        "You must be at least 18 years old to vote in Australia.",
    )

print()

print_dialogue("Australian Legal Drinking Age Verification")
if age >= 18:
    print_dialogue(
        "You are eligible to drink alcohol, but drink responsibly.",
        "Remember to always follow the legal drinking age requirements in your area.",
    )

else: 
    print_dialogue(
        "You are ineligible to drink alcohol. You must be at least 18 years old.",
        "Remember to always follow the legal drinking age requirements in your area.",
    )

print()

print_dialogue("Australian Driver's Licence Age Verification")
if age >= 18:
    print_dialogue(
        "You are eligible to apply for a driver's licence.",
        "Remember to always follow the legal driving age requirements in your area.",
    )

elif age >= 16:
    print_dialogue(
        "You are eligible for a learner's permit.",
        "Remember to always follow the legal learner's permit requirements in your area.",
    )

else:
    print_dialogue(
        "You are not eligible to apply for a driver's licence or a learner's permit.",
        "You must be at least 16 years old to apply for a learner's permit and 18 years old to apply for a driver's licence in Australia.",
    )

print_dialogue(
    "This age verification process varies by state, territory, and country, "
    "so it's important to check the specific requirements in your area."
)

# The elif statement checks if the user is at least 16 years old, allowing them to apply for a learner's permit.

# Remember, laws and regulations regarding age verification may vary by country or region, so it's important to check the specific requirements in your area.

# This project uses Australia's legal age requirements for voting, drinking alcohol, and acquiring a driver's licence as examples.

# This Python mini project uses Australia's laws and jurisdictions. Laws, regulations, and legal age requirements vary by territory and state in Australia, so it's important to check the specific requirements in your area.
