"""
Using the Chi-square Statistic
The chi-square statistic allows compare how closely a shift of the English frequency
distribution matches the frequency distribution of the secret message. Here's an
algorithm for computing the chi-square statistic:

    Let ef(c) stand for the english frequency of some letter of the alphabet
    Let mf(c) stand for the frequency of some letter of the message
    For each possible shift s between 0 and 25:
      For each letter c of the alphabet
        Compute the sum of squares of mf((c + s) mod 26) divided by ef(c)

That is, for a given character, say 'a', we compute the square of the frequency of
that character shifted by one of the possible Caesar shifts and then divide it by the
English frequency of that character. For a given shift, say 5, we do this for each of
the 26 letters in the alphabet. We thereby get 26 different chi-square values. The
shift s for which the number ChiSquare(s) is smallest is the most likely candidate
for the shift that was used to encipher the message.

"""