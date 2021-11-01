# File I/O

- Create account using Email, Username and Password. Store the user details in the simple txt file locally
- Login using the Username and Password
- Validate the credentials against the text file

## Concepts

**File Read & Write**

- _with_ keyword is used to open the file. The main advantage of using the "with" keyword is, the user no need to close the file explicitly by calling _close()_ method.
- _open()_ method is used to open the file during read and write

**File Modes**

- _a_ mode opens the file for append. It appends to the end of the file. If the file doesn't exists, it will create a new file for writing.
- _r_ mode is used to read the file from the beginning. This is the default mode.

**Read file line by line**

- use _for_ loop to read the file line by line

**Password**

- _pwinput_ package is used to get the password input from the user, so that it masks the password (\*) while typing
