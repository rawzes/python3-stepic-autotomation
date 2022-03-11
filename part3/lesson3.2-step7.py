

# concatenation example
text = 'abracadabra'
print('The error was found: ' + text + ". Please fix it!")

#  more advanced approach: using  str.format
print("Let's count together: {}, {} and {}".format('one', 'two', 'three'))

#  more convenient way: f-strings

one1 = 'one'
two1 = 'two'
three1 = 'three'
print(f"Let's start counting one more time from {three1} to {one1}")

actual_result = 'abracadabra'
expected_result = 'some text'
print(f'Got wrong result: {actual_result} when expected: {expected_result}, please take a look')

print(f'It is possible to paste operators into f-strings: 2+4 = {2+4}')
