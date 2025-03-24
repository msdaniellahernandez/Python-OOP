class SerialGenerator:
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
    def __init__(self, start):
        """Initialize the serial generator with a starting number."""
        self.start = start
        self.current = start

    def generate(self):
        """Generates the next serial number.
        
        Returns:
            int: The next serial number in sequence.
        """
        next_serial = self.current
        self.current += 1
        return next_serial

    def reset(self):
        """Reset the serial generator to the original starting number."""
        self.current = self.start
serial = SerialGenerator(start=100)
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
serial.reset()
print(serial.generate())  # Output: 100
