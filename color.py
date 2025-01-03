class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    print(f"{Color.HEADER}HEADER{Color.ENDC}")
    print(f"{Color.OKBLUE}OKBLUE{Color.ENDC}")
    print(f"{Color.OKCYAN}OKCYAN{Color.ENDC}")
    print(f"{Color.OKGREEN}OKGREEN{Color.ENDC}")
    print(f"{Color.WARNING}WARNING{Color.ENDC}")
    print(f"{Color.FAIL}FAIL{Color.ENDC}")
    print(f"{Color.BOLD}BOLD{Color.ENDC}")
    print(f"{Color.UNDERLINE}UNDERLINE{Color.ENDC}")

if __name__ == "__main__":
    main()
