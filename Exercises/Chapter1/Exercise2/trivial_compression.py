from solution import BitSequence

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_sequence: BitSequence = BitSequence()
        for i, nucleotide in enumerate(gene.upper()):
            if nucleotide == "A":
                self.bit_sequence.append(0b00)
            elif nucleotide == "C":
                self.bit_sequence.append(0b01)
            elif nucleotide == "G":
                self.bit_sequence.append(0b10)
            elif nucleotide == "T":
                self.bit_sequence.append(0b11)
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for bits in self.bit_sequence:
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backwards

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_sequence)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))