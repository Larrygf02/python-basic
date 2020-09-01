def find_phonenumber(phonebook, name):
    for n,p in phonebook:
        if n == name:
            return p
    return None

phonebook = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555"),
]

print(find_phonenumber(phonebook, "John Doe"))


phonebook = {
    "John Doe": "555-555-5555",
    "Albert Einstein" : "212-555-5555",
}

print(phonebook["John Doe"])
