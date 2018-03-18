

def main():
    x = 5
    print(x)
    do_stuff(x)
    print(x)
    print(y)

def do_stuff(y):
    print(y)
    y = 7
    print(y)

    # functions calling functions don't pass scope

if __name__ == '__main__':
    main()
