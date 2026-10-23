#Project 7 — Text Compression Using Character Runs
text = input("Enter a string: ")
if text == "":
    print("Please enter a non-empty string")
else:
    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1
    encoded += text[-1] + str(count)
    print("Original string:", text)
    print("Encoded string:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) < len(text):
        print("Compression is beneficial")
    else:
        print("Compression is not beneficial")