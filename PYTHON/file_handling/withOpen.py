# If you use 'with' when handling python files you are not required to use the close () function.
with open("example.txt") as f:
    print(f.readlines())
    print(f.readline())
    print(f.read())

# 2
# Loops

with open("example.txt") as f:
    for x in f:
        print(x)


# Append
# When appending we us 'a' to add text to the end of the file

with open("example.txt", "a") as f:
    f.write("Added this text")

# write
# We use 'w' to overwrite
# This overwrite the whole content

with open("example.txt", "w") as f:
    f.write("Overwritten the text!!")
