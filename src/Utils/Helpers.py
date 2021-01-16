import string
import random

class Helpers:

    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomName(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(5))
    def randomLowID(self):
        """Generate a random lowID of digits """
        return int(''.join([str(random.randint(0, 9)) for _ in range(7)]))

    def randomClubID(self):
        """Generate a random clubLowID of digits """
        return int(''.join([str(random.randint(0, 9)) for _ in range(7)]))