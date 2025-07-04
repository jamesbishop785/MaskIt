from datetime import datetime

def defang_ip(ip: str) -> str:
    return ip.replace('.', '[.]')

def defang_email(email: str) -> str:
    return email.replace('@', '[@]').replace('.', '[.]')

def defang_url(url: str) -> str:
    url = url.replace('http://', 'hxxp://').replace('https://', 'hxxps://')
    return url.replace('.', '[.]')

def refang_ip(ip: str) -> str:
    return ip.replace('[.]', '.')

def refang_email(email: str) -> str:
    return email.replace('[@]', '@').replace('[.]', '.')

def refang_url(url: str) -> str:
    url = url.replace('hxxp://', 'http://').replace('hxxps://', 'https://')
    return url.replace('[.]', '.')

def log(action: str, input_val: str, output_val: str, history: list) -> None:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("maskit_log.txt", "a") as logfile:
        logfile.write(f"[{timestamp}] {action}\n")
        logfile.write(f"Input:  {input_val}\n")
        logfile.write(f"Output: {output_val}\n\n")

    history.append((action, input_val, output_val))
    print(f"\n[LOG] {action}")
    print(f"Input:  {input_val}")
    print(f"Output: {output_val}")

def show_history(history: list) -> None:
    if not history:
        print("\n[History is empty]\n")
        return
    print("\n=== History Log ===")
    for i, (action, input_val, output_val) in enumerate(history, 1):
        print(f"{i}. {action}")
        print(f"   Input:  {input_val}")
        print(f"   Output: {output_val}")
        print("-" * 30)
    print()

def main():
    print("=== Defang/Refang Tool ===")
    history = []

    options = {
        "1": ("Defang IP", defang_ip),
        "2": ("Defang Email", defang_email),
        "3": ("Defang URL", defang_url),
        "4": ("Refang IP", refang_ip),
        "5": ("Refang Email", refang_email),
        "6": ("Refang URL", refang_url),
    }

    while True:
        print("\nSelect an option:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("7. Show History")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice in options:
            action, func = options[choice]
            user_input = input(f"Enter value to {action.lower()}: ").strip()
            result = func(user_input)
            log(action, user_input, result, history)

        elif choice == "7":
            show_history(history)

        elif choice == "8":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
