# Privacy Data Encryption and Decryption App

This Python application is designed to encrypt and decrypt sensitive data using the Fernet encryption from the `cryptography` library. The application utilizes the `tkinter` library to provide a simple graphical user interface (GUI) for users to interact with.

## Main Features:
- Encryption: The application allows users to encrypt their sensitive data by providing the data and a master key. The data is encrypted using Fernet encryption and saved in a text file for later access.
- Decryption: Users can decrypt the encrypted data by entering the corresponding key title and the master key.

## How to Use:
1. The application requires a pre-defined `MasterKey` to gain access to the encryption and decryption functionalities.
2. Enter the data you want to encrypt in the provided input field and click the "Encrypt" button. The data will be encrypted using Fernet encryption and saved in a text file.
3. To decrypt the encrypted data, enter the corresponding key title and the `MasterKey` in the appropriate input fields, then click the "Decrypt" button. The decrypted data will be displayed on the screen.

**Note:** Ensure that you keep the `MasterKey` secure, as it is crucial for both encryption and decryption operations.

The application features a simple and user-friendly GUI with background images and buttons for easy interaction. In case of any errors during encryption or decryption, an "Oops" error message will be displayed.

Please make sure to keep the necessary image files (error.png, dataprivacybg.png, encryptButton.png, decryptButton.png) in the same directory as the script for the GUI elements to display correctly.

Enjoy using the Privacy Data Encryption and Decryption App to secure your sensitive information!
