# FUTURE_CS_02
it,s a code for password analyzer using only python and its a part of my internship program.


**Password Strength Analyzer Tool - Documentation**

**1. Introduction**
The Password Strength Analyzer Tool is designed to evaluate the strength of user-entered passwords, hash them securely using SHA-256, and encrypt them using symmetric encryption (Fernet). The tool provides a graphical user interface (GUI) built with Tkinter, ensuring ease of use while maintaining security best practices.

**2. Features**
- Password strength assessment based on predefined security criteria.
- SHA-256 hashing for password security.
- Fernet encryption for secure password storage.
- GUI-based interactions for user-friendly operation.
- Reset and exit functionalities for convenience.

**3. Technologies Used**
- **Python** for scripting.
- **Tkinter** for GUI development.
- **Hashlib** for SHA-256 hashing.
- **Cryptography (Fernet)** for symmetric encryption.
- **Regular Expressions (re module)** for password validation.

**4. Algorithm Explanation**

**4.1 Password Strength Evaluation**
The password strength checker applies the following validation rules:
- Minimum length of 8 characters.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one digit.
- At least one special character (@#$%^&*).

Depending on these conditions:
- Weak passwords fail one or more criteria.
- Moderate passwords meet minimum requirements.
- Strong passwords exceed 12 characters while fulfilling all conditions.

**4.2 Password Hashing**
- The entered password is encoded into bytes.
- It is hashed using **SHA-256**, a secure cryptographic hashing algorithm.
- The hash output is displayed to the user for verification.

**4.3 Password Encryption**
- A symmetric encryption key is generated using **Fernet** from the Cryptography module.
- The entered password is encrypted using the generated key.
- The encrypted password is displayed in its encoded form.

**4.4 Reset and Exit Functionality**
- The Reset button clears the password entry field and resets all output labels.
- The Exit button terminates the application safely.

**5. Effectiveness of the Algorithm**
- **SHA-256 hashing** ensures that passwords are stored securely without reversible decryption.
- **Fernet encryption** allows secure password storage, making it difficult for unauthorized users to access plaintext passwords.
- **Password strength rules** enforce best practices, reducing the likelihood of weak passwords.
- **User-friendly interface** simplifies the process of password validation, hashing, and encryption.

**6. Conclusion**
The Password Strength Analyzer Tool serves as a comprehensive solution for evaluating and securing passwords. By incorporating hashing, encryption, and validation mechanisms, it enhances password security while maintaining an intuitive user experience. This tool is beneficial for both individual users and organizations aiming to improve their password security practices.


