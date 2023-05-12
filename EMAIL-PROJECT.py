email = input("Enter your Email : ")
a = 0
b = 0
x = 0
if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email:
            if email.count("@") == 1:
                if email[0].isalpha():
                    if email[:email.index("@")]:
                        if email[email.index("@") + 1:email.index(".")]:
                            if email[email.index(".") + 1:]:
                                if 1 < len(email[email.index(".") + 1:]) < 5:
                                    if (email[email.index(".") + 1:]).isalpha() and (email[email.index(".") + 1:]).islower():
                                        b = b + 1
                                        if (email[:email.index("@") + 1:email.index(".")]).isalnum():
                                            for i in email[:email.index("@")]:
                                                if i.isalnum():
                                                    pass
                                                elif i == "_":
                                                    x = x + 1
                                                else:
                                                    a = a + 1
                                        else:
                                            print("Wrong Email12")
                                    else:
                                        print("Wrong Email0")
                                else:
                                    print("Wrong Email9")
                            else:
                                print("Wrong Email8")
                        else:
                            print("Wrong Email7")
                    else:
                        print("Wrong Email6")
                else:
                    print("Wrong Email5")
            else:
                print("Wrong Emai4")
        else:
            print("Wrong Email3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
if a != 0 or (x >= 2):
    print("Wrong Email")
if (a == 0) and (b != 0) and (x < 2):
    print("right email")
