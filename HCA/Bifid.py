"""  https://www.geeksforgeeks.org/bifid-cipher-in-cryptography/

Bifid Cipher in Cryptography

This cipher technique considered more secure compared to other substitution algorithms reason being it breaks the message apart into two separate streams and then recombines them. It is a combination of the Polybius square with the transposition and uses fractionation to achieve diffusion. This encrypting technique invented by Felin Delastelle. It just only ever used by amateur cryptographers.

Encrypting Algorithm:
For this cipher technique algorithm, we use the 25-letter “key-Square” table.

Example:


   1   2   3   4   5
1  R   A   N   C   H

2  O   B   D   E   F

3  G   I   K   L   M

4  P   Q   S   T   U

5  V   W   X   Y  Z

Here we merged J with the I because we are using a 5 X 5 square key matrix so we can use only 25 characters out of the 26.

Let us take “RAMSWARUP IS THE STUDENT OF THE NIT CALICUT” as our plain text.

Step-1:
Now find each letter of the plain text in the key-square and write the corresponding row number and column in two separate lines. For example, our first letter is the “R” which is present in the first row and first column, so the key cipher text key value for it is “1-1”.

        RAMSWARUP     IS       THE     STUDENT      OF      THE      NIT     CALICUT
ROW :   113451144     34       412     4442214      22      412      134     1133144
COL :   125322151     23       454     3453434      15      454      324     4242454

Step-2:
Now select a certain amount of size (this is called the period) which indicate how many key values we are going to take. for example in this example take the block size is 5. So divide the values in the block of the period.

ROW:   11345   11443   44124  44221  42241   21341  13314  4
COL:   12532   21512   34543  45343  41545   43244  24245  4

Step-3:
Now merge the values of rows and columns. Rows values followed by the columns. Final values after combining the values of rows and columns:

1134512532    1144321512     4412434543    4422145343    4224141545     2134143244     1331424245   44

Step-4 (Final Step):
Now select pair values from the final combined values and take corresponding character value from the key-square matrix. (first value indicates the row number and second value indicates the column values).

For example first taken value is 11 which indicates the character “R” and then we took 34 which is representing the character “L”.

CIPHER-TEXT:  RLVFIRTIHATASUSTBCXSQECHUOLCITNGQQUT



"""