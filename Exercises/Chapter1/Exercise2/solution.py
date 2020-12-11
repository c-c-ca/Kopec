from typing import List

class BitSequence():

    def __init__(self) -> None:
        self.bit_string: int = 1

    def append(self, bits: int) -> None:
        if bits < 0b00 or bits > 0b11:
            raise ValueError("Invalid bits:{}".format(bits))

        self.bit_string <<= 2
        self.bit_string |= bits
    
    def __getitem__(self, key: int) -> int:
        if key > self.bit_string.bit_length() // 2 - 1:
            raise IndexError()
        
        return self.bit_string >> key * 2 & 0b11
