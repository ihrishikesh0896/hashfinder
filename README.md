# hashfinder
Basic md5 hash finder

In this code, the crack_password function takes a password hash, a character set, and the maximum password length as inputs. It uses the itertools.product function to generate all possible combinations of characters from the given character set up to the specified password length. The generated passwords are then hashed using the MD5 algorithm and compared to the provided password hash.

To use the code, you need to run it and provide the necessary inputs. The program will attempt to crack the password by generating and hashing different combinations of characters. If a match is found, it will print the password; otherwise, it will indicate that the password was not found.

Please note that this is a basic example, and real-world password cracking involves more advanced techniques, considerations, and security implications.