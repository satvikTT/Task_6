import re
import hashlib
import requests

def check_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add uppercase letters for better security.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add lowercase letters for better security.")

    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Include numbers to strengthen your password.")

    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks.append("Add special characters like @$!%*?& for more strength.")

    if strength >= 4:
        return "Strong", remarks
    elif strength == 3:
        return "Moderate", remarks
    else:
        return "Weak", remarks

def check_pwned_api(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        return False, "Error reaching HaveIBeenPwned API."

    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True, f"⚠️ This password has been seen {count} times in data breaches!"
    return False, "✅ This password hasn't been found in known breaches."

def main():
    password = input("Enter your password to check: ")
    strength, tips = check_strength(password)
    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Tips to improve your password:")
        for tip in tips:
            print(" -", tip)

    check_leak = input("\nCheck if this password has been leaked? (y/n): ").lower()
    if check_leak == 'y':
        leaked, message = check_pwned_api(password)
        print(message)

if __name__ == "__main__":
    main()
