# Email Validation Code

This repository contains a Python script that validates an email address entered by the user. The script checks various conditions to determine if the email is valid or not.

## Usage
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine or download the [script file](script.py) directly.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the following command:

   ```shell
   python script.py
   ```

5. The script will prompt you to enter your email address.
6. Enter the email address and press Enter.
7. The script will validate the email address based on the following conditions:

   - The email address must be at least 6 characters long.
   - The first character of the email address must be an alphabet.
   - The email address must contain exactly one "@" symbol.
   - There should be characters before and after the "@" symbol.
   - There should be characters after the "." symbol.
   - The length of characters after the "." symbol should be between 2 and 4.
   - The characters after the "." symbol should be all lowercase alphabets.
   - The email address should not contain more than one underscore character.
   - The characters before the "@" symbol can only be alphanumeric.
   - The email address should not contain any special characters other than underscore.

8. Based on the validation results, the script will display one of the following messages:

   - If the email address is valid: "Right email"
   - If the email address is invalid: "Wrong email"

## Contributing
Contributions to this repository are welcome. If you find any issues or want to enhance the functionality, feel free to submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
