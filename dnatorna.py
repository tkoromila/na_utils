"""
Convert DNA seq to RNA.
"""

def rna(seq):
    """Conv a DNA seq to RNA."""

    #Dtermine if te orifinal seq was uppercase
    seq_upper = seq.isupper()

    #Convert to lowercase
    seq = seq.lower()

    #Swap out 't' for 'u:'
    seq = seq.replace('t', 'u')

    #Return upper or lower, dep on input
    if seq_upper:
        return seq.upper()
    else:
        return seq
def reverse_rna_complement(seq):
    """Conv a DNA seq into its reverse comp as RNA"""

    # Detremine if the original seq was uppercase
    seq_upper = seq. isupper

    #Rev seqseq = seq[::-1]

    #conv to uppercsre
    seq = seq.upper()

    #compute complement_base
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    #Return in appropriate complement_baseif seq_upper
    if seq_upper:
        return seq.upper()
    else:
        return seq
