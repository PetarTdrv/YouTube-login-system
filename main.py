import webbrowser

print("----------------------Login to YouTube----------------------")
nic = input("\nEnter your new username: ")
pas = input("Enter your new password: ")
re_pas = input("Reenter your new password: ")

nickname = nic
password = pas

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RED2 = '\033[31m'
RESET = '\033[0m'


wrong_tries_count = 0

while True:
    if re_pas == pas:
        print(f"\n{GREEN}Succesfully maked your account.{RESET}")
        log = input("\nDo you want to continue(Yes/No): ")
        if log == "Yes":
            while True:
                name = input("\nEnter your username: ")
                key = input("Enter your password: ")
                if name != nickname:
                    print(f"\n{RED}Wrong nickname.{RESET}")
                    wrong_tries_count += 1
                elif key != password:
                    print(f"\n{RED}Wrong password.{RESET}")
                    wrong_tries_count += 1
                elif name == nickname:
                    if key == password:
                        print(f"\n{GREEN}Succesfully loged.{RESET}")
                        url= 'https://www.youtube.com/'
                        webbrowser.open_new_tab(url)
                        exit()

                if wrong_tries_count == 3:
                    print(f"\n{CYAN}Sorry used all attempts.{RESET}")
                    exit()

        elif log == "No":
            break

    elif re_pas != password:
        print(f"\n{RED}Wrong password.{RESET}")
        re_pas = input("Reenter your new password: ")
        if re_pas != password:
            print(f"\n{RED2}Try again.{RESET}")
            break
