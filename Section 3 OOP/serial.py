"""Python serial number generator."""

class SerialGenerator:

    def __init__(self, start=0):
        self.start = self.next = start

    def generate(self):
        self.next += 1
        return self.next - 1
    
    def reset(self):
        self.next = self.start


    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())
