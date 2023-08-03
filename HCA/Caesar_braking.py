# From: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm

# Hacking of Caesar Cipher Algorithm
#
# The cipher text can be hacked with various possibilities.
# One of such possibility is Brute Force Technique, which involves trying every possible decryption key.
# This technique does not demand much effort and is relatively simple for a hacker.
#
# The program implementation for hacking Caesar cipher algorithm is as follows −

import Caesar

message = 'Vgiq se hud cozn lobk jufkt rowaux pamy.' #encrypted message
# message = 'Ymzj ul yri silx wfi yarvcg jrr yri Alczv efxcv yzekj.' #encrypted message, fra FE-fun
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Method 1 - I have no clue what it's doing - can you help here M0LLY ...
print("\nMethod 1:")
for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))

# Method 2 - Try decrypting 26 ways and see what looks like english text
print("\nMethod 2:")
bol_showall = True
lst_language = ['am', 'era', 'my', 'liquor', 'jugs']  # For a real routine you should provide a list of hundreds of words, frequent in your language.
lst_scores = list()  # list of tuples of (score, key)
m2 = ""  # message-2, a local clean copy of the message, only including letters and wide-spaces
for char in message:
   if char.upper() in LETTERS or char == ' ':
      m2 += char
for key in range(len(LETTERS)):
   cleartext = Caesar.decrypt(m2, key)
   if bol_showall:
      print(f" - loop: {key} -> {cleartext[:64]}")
   score = sum([w in lst_language for w in cleartext.split(' ')])
   if score > 0:
      lst_scores.append((score, key))
best_key = sorted(lst_scores, reverse=True)[0][1]
print(f"most likely key: {best_key} -> {Caesar.decrypt(message, best_key)}")
