# Accessing Strings


Instructions: You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4


Psuedocode:





            BEGIN
              DECLARE array of vowels = ['a', 'e', 'i', 'o', 'u']
              DECLARE count = 0

              PROMPT user_input
              MAKE the user_input lowercase

              FOR each of the letter in user_input
                IF user_input matches one in vowels
                  count = count + 1
                ENDIF
              ENDFORLOOP

              PRINT COUNT

            END