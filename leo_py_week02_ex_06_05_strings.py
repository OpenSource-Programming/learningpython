# Exercise 6.5

text = "X-DSPAM-Confidence:    0.8475"

extrac_value = text[text.find(":")+1:]

print(float(extrac_value))
