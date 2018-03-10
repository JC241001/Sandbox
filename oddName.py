"""Gerard Djian"""


def main():  # Test skip_letter() function
    for name in ["Harold", "Tom", "", "Constance", "Elizabeth", "Dictionary"]:
        skip_letter(name)


def skip_letter(persons_name):
    # persons_name = input("Enter your name: ")
    while persons_name == "":
        print("Must enter something")
        persons_name = input("Enter your name: ")

    modified_persons_name = persons_name[::2]
    print("Every second letter is: {}".format(modified_persons_name))


if __name__ == '__main__':
    main()
