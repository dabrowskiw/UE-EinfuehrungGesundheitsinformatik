def dostuff(what):
    print("You want me to do what? " + what + "?")

print("Hi there, thanks for importing mymdolues!")

if __name__=="__main__":
    from sys import argv
    print(argv)
    if argv[1] == "Hi":
        print("Hello to you, too!")