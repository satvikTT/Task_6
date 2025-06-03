# Password Strength Evaluation ( Task - 6 )

---
## Objective
To understand what makes a password strong and evaluate its robustness using free online password strength checkers. You will explore password complexity, analyze feedback from tools, and summarize key takeaways about creating secure passwords.

---
## Tools Accessed

### Free online password strength checking tools:
- PassowrdMeter
  ```bash
  https://passwordmeter.com/
  ```
- How Secure Is My Password
  ```bash
  https://howsecureismypassword.net/
  ```
- Kaspersky Password Checker
  ```bash
  https://password.kaspersky.com/
  ```
- Bitwarden Password Tester
  ```bash
  https://bitwarden.com/password-strength/
  ```
- Security.org Password
  ```bash
  https://www.security.org/how-secure-is-my-password/
  ```
- Password Monster
  ```bash
  http://passwordmonster.com/
  ```

---
## Deliverables

1. A list of the passwords you tested (do NOT use real or reused passwords).
   ```bash
   AdamJohn@2705
   ```
   ```bash
   SatvikkkBhgt@2705
   ```
   ```bash
   Hello@123
   ```
   ```bash
   MyNameIsJOKER@13579#
   ```
   ```bash
   PswdMonster@91347#
   ```
   ```bash
   fName@lName#1970
   ```
   
2. Screenshots or descriptions of the tool feedback/scores.
   
3. Best practices for creating strong passwords
   
   - Use a Long Password
     - Aim for at least 12–16 characters.
     - Longer passwords are significantly more secure.
   - Include a Mix of Character Types
     - Use a combination of:
       - Uppercase letters (A–Z)
       - Lowercase letters (a–z)
       - Numbers (0–9)
       - Special characters (!@#$%^&*()-_=+[]{};:,.<>?)
   - Avoid Common Words and Patterns
     - Do not use easily guessable words like "password", "123456", or "qwerty".
     - Avoid using personal information (like your name, birthday, or pet’s name).
   - Use Passphrases Instead of Passwords.
     - Create a passphrase using unrelated words, like:
         ```bash
         "PurpleRain$Monkey!Bridge1984"
         ```
   - Avoid Reusing Passwords
     - Never use the same password across multiple accounts.
     - If one account is compromised, others could be at risk.
   - Change Passwords if Compromised
     - Only change passwords when there's a reason to (e.g., a data breach or suspicious activity).
     - Avoid frequent unnecessary changes, which can lead to weaker, more memorable passwords.
   - Use a Password Manager
     - Store complex passwords securely.
     - Allows you to use unique, strong passwords for every account without needing to remember each one.
   - Enable Two-Factor Authentication (2FA)
     - Even strong passwords can be compromised. 2FA adds an extra layer of protection.
   - Avoid Password Hints That Give Away the Password
     - Hints should not make the password guessable.
   - Use Random Generators for Critical Accounts
     - For highly sensitive accounts, consider using a random password generator (built into most password managers).
       
4. Summary of the impact of password complexity on overall security.
---
## Outcome

- Identify the key traits of a strong password.

- Understand how password strength is evaluated.

- Recognize common threats to password security.

- Apply best practices to create and manage secure passwords.
  
---
## Tips

- Don’t test real personal passwords.

- Compare feedback for same password from multiple tools for better understanding.

- Enable breach alerts to know if your passwords are compromised.

- Avoid saving passwords in browsers without encryption.

- Generate random passwords instead of creating your own.

- Audit passwords regularly for weaknesses or reuse.

---
## Summary
### How Password Complexity Affects Security

Password complexity plays a crucial role in defending against cyber attacks by making passwords significantly harder to guess, crack, or predict.

1. Length Increases Strength
   - The longer the password, the more combinations an attacker must try.
   - Each additional character exponentially increases the difficulty of brute-force attacks.

2. Character Variety Matters
   - Including a mix of uppercase and lowercase letters, numbers, and special symbols creates a much larger pool of possible combinations.
   - This variety makes brute-force and dictionary attacks far less effective.

3. Avoiding Predictability
   - Simple passwords (like “Password123” or “qwerty”) are commonly used and easily guessed.
   - Attackers use precompiled lists of such passwords in dictionary attacks, making weak passwords a big risk.

4. Randomness Defeats Patterns
   - Randomly generated passwords lack recognizable patterns, making them harder for both humans and algorithms to guess.

5. Time and Resources
   - Complex passwords increase the time, computing power, and effort required for an attacker to succeed.
   - Often, this added difficulty deters attacks entirely or causes them to fail.

✅ ** Stronger complexity = Better protection **
❌ ** Weak/simple passwords = Easy targets for attackers **

### Conclusion
Using complex passwords is one of the simplest and most effective ways to protect personal and organizational data from unauthorized access.

---
## Additional attachment
**pswd_checker.py**
** Python script designed to perform **to check the strength and safety of a password by:-
1. Evaluating Strength
   - Assesses if the password includes uppercase, lowercase, numbers, special characters, and is at least 8 characters long.
   - Rates the password as Weak, Moderate, or Strong and provides tips for improvement.

2. Checking Data Breaches
   - Optionally checks if the password has been leaked in known data breaches using the HaveIBeenPwned API.

This tool helps users create more secure passwords and avoid using compromised ones.
---



