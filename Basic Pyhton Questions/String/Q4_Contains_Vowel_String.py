

s='MyNameisJackou'
VW='aeiou'

if all( i in s.lower() for i in VW ):
    print('All Vowels')
else:
    print('All are not vowels')