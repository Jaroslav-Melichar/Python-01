from datetime import datetime
name = input('Whats your name ? ');
age = int(input('Your age ? '));
Years = int((100-age) + datetime.now().year);
print ('You will be 100 years old in the year : %s' % (Years));