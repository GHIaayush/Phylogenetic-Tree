
#importd the genome file
from genome import*
#imports the tree file
from tree import*
"""
File:phylo.py
    Author: Aayush Ghimire, Date:05/2/2018,
    Purpose: To construct phylogenetic trees starting from
    the genome sequences of a set of organisms.
"""

"""
This function ask the user for the input file, size of ngram
they wish to make 
"""
def ask_user():
    """
    This function ask the user about the size of ngram they wish to make
    and returns the ngram as the int value and file after opening it

    PARAMETER: NONE

    RETURN: the file and int value is returned

    PRE-CONDITION: it ask the input from user

    POST-CONDITION: the legit user input will be converted to int for
    n gram size and file will be returned

    """
    user_input = input('FASTA file: ')
    N_size = input('n-gram size: ')#ask input
    try:
        open_file = open(user_input)#opens
    except IOError:
        print("ERROR: could not open file " + user_input)
        exit(1)
    try:
        N_size = int(N_size)
    except ValueError:
        print("ERROR: Bad value for N")
        exit(1)

    return open_file, N_size
"""
This function process the file
"""
def read_fasta(open_file):
    """
    This file takes opened file passed by the user and process
    it

    PARAMETER: the opened file is passed as a parameter

    RETURN: the virus list i.e the list of the id and genome is returned

    PRE-CONDITION: the file passed is just opened

    POST-CONDITION: virus list is the list that contains organism  id and
    genome in a sequence
    """
    virus_list = []#new list to store
    genome_str = ""#new str to concat
    for line in open_file:
        #loops through file
        line = line.strip()#Remove all empty lines and pace
        if line != "":
            #print(line)
            if line[0][0] == ">":#is id line
                if genome_str != "":#checks for concatenation
                    virus_list.append(genome_str)#append in a list
                    genome_str = ""#appends and reset it
                virus_list.append(line)#append a details

            elif (line[0][0] == "A" or line[0][0] == "C" or
                line[0][0] == "G" or line[0][0] == "T"):#checks for genome line
                genome_str += line#concat the str
    virus_list.append(genome_str)#append the last line
    return(virus_list)#gets all the file

"""
This function creates a genome object and a tree object.
"""
def create_genome_tree_obj(virus_list,N_size):
    """
    This fucntion takes a list, the int value input by the user
    and makes a genome object which has id , and set a sequence
    and tree object which has a string as id and left and right
    as none. It also creates a list and dictionary that has
    key as a id(type string) and value as a genome object.Two list
    that stores genome and tree object

    PARAMETERS:the cleaned list which has id and genome string in a
    sequencce and N-gram size input of the user is passed as a
    parameter

    RETURNS: the genome list, dictionary and tree_list are returned

    PRE-CONDITION: parameter passed are type list and int value

    POST-CONDITION: list and dictionary are returned
    """
    genome_list = []#to store genome object
    tree_list = []#to store tree object
    genome_dic = {}#to store id associated with object
    for i in range(0,len(virus_list),2):
        #loops and step by two because it has id and genome seq
        virus_id = virus_list[i].split()#split the id
        virus_id[0] = virus_id[0].replace(">","")#replace ">"
        seq = virus_list[i+1]#gets a sequence
        tree = Tree()#creates tree
        tree.set_id(virus_id[0])#sets if
        tree.add_list(virus_id[0])#add in a list
        tree_list.append(tree)#append tree object in list
        gd = GenomeData()#create genome data object
        gd.set_id(virus_id[0])#sets id
        gd.set_sequence(seq)#sets sequence
        gd.set_ngrams(N_size)#sets n grams
        if virus_id[0] not in genome_dic:#checks if key exist
            genome_dic[virus_id[0]] = gd#creates a key and value 
        genome_list.append(gd)#append in dicionary
    return genome_list, genome_dic, tree_list

"""
This function checks the maxim similarity between the two trees
among all the trees in the trees list
"""
def tree_similarity(genome_list,genome_dic,tree_list):
    """
    This checks the similarity between the all possible tree objects and
    returns the maximum similarity and that two tree object as a tuple

    PARAMETER: genome list, genome dic and tree list are passed as a
    parameter

    RETURN: max value of similarity and two tree which got the maximum
    similarity is returned

    PRE-CONDITION: list and dictionary are passed

    POST-CONDITION: int and tuple is returned
    """
    i = 0#sets as  for while loop 
    max_value = -1#sets max as -1
    max_tree = tuple()#create an empty tuple
    while len(tree_list) != i:#
        key1 = tree_list[i]
        j =  i + 1
        while len(tree_list) != j:
            key2 = tree_list[j]
            #calls a helper function
            val_max , tree_max = seq_set_sim(key1,key2,genome_dic)
            if val_max > max_value :
                max_value = val_max
                max_tree = tree_max

            j += 1
        i += 1
    return max_value,max_tree

"""
This function takes a tree list. Calls a hepler function
And combines two tree which has maximum similarity until the list
has one single tree object. 
"""

def make_list(genome_list,genome_dic,tree_list):#,max_value,max_tree):
    """
    This function combines two tress which has the maximum similarity. It creates
    a new tree object. It removes those two tree object from the tree list.
    """
    while len(tree_list) > 1:#till there is one element in list
        max_value , max_tree =tree_similarity(genome_list,genome_dic,tree_list)
        tree = Tree()#new tree object
        if str(max_tree[0]) < str(max_tree[1]):
            tree._left = max_tree[0]
            tree._right = max_tree[1]
        else:
            tree._right = max_tree[0]
            tree._left = max_tree[1]
        tree.join_list(max_tree[0].get_list(),max_tree[1].get_list())
        tree_list.append(tree)
        
        tree_list.remove(max_tree[0])#reoves from list
        tree_list.remove(max_tree[1])#removes from list
    return tree_list#return tree list

"""
This function computes the jacard index of the sets and returns
the maximum value of similarity and tuple of tree object which has
highest similarity
"""
def seq_set_sim(key1,key2,genome_dic):
    """
    This function computes the jacard index of two sets and
    returns the highest similarity value and tuple of tree
    object which has highest similarity
    """
    new = -1
    max_tree = tuple()
    var1 =(key1.get_list())
    var2 =(key2.get_list())
    #loops through list
    for i in range(len(var1)):
        for j in range(len(var2)):
            s1 = genome_dic[var1[i]].get_ngrams()
            s2 = genome_dic[var2[j]].get_ngrams()
            #computes the similarity
            similarity= (float (len(s1.intersection(s2)))
                         / float (len(s1.union(s2))))
            if similarity > new:
                new = similarity
                max_tree = (key1,key2)
    #highest value and tree tuple
    return new, max_tree

"""
This is the main of the program.It calls all the function in the
program.
"""
def main():
    #ask the user in the function and stores the return value
    open_file, N_size = ask_user()
    #store clean list
    virus_list = read_fasta(open_file)
    #store genome_list dictionary and list
    genome_list, genome_dic, tree_list = (create_genome_tree_obj
                                          (virus_list,N_size))
    #makes the final tree, and return it 
    final_tree = make_list(genome_list, genome_dic, tree_list)
    #prints the tree
    print(final_tree[0])
    

main()
