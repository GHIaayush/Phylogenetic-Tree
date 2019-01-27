"""
File:genome.py
    Author: Aayush Ghimire, Date:05/2/2018.
    Purpose: To construct a class Genome data to make a genome data
    object for each organism. It is exported to main file phylo.py
"""
"""
This is the helper file that has the Genomedata object. It is exported
to the phylo file.
"""
class GenomeData:
    """
    This class creates a instant of genomedata object.It initialize the
    attribute of the genome data and have specific setter and getter

    PARAMETER: NONE

    RETURN: getter method has their specific return

    PRE-CONDITION: class is consructed with its attribute

    POST-CONDITION: it creates a genome data object
    """
    def __init__(self):
        #intialize the atrribute
        self._id = None
        self._sequence = None
        self._ngrams = None

    #sets the id
    def set_id(self,id):
        self._id = id

    #sets the sequence
    def set_sequence(self,sequence):
        self._sequence = sequence

    #sets the ngrams
    def set_ngrams(self,n):
        seq = self._sequence
        self._ngrams = (set(seq[i:i+n] for i in
                            range(0,len(seq)) if len(seq[i:i+n]) == n))

    #getter to get the id
    def get_id(self):
        return self._id

    #getter to get the sequence
    def get_sequence(self):
        return self._sequence

    #getter to get the sequence
    def get_ngrams(self):
        return self._ngrams

    #str method to debug i printed out the id to see whats going on
    def __str__(self):
        return str(self._id)
