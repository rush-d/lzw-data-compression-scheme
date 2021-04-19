# LZW Encoder Algorithm

from sys import argv
from struct import *

# taking the input file and the number of bits from command line
inputFile, n = argv[1:]       

# defining the maximum table size
maxTableSize = pow(2,int(n))   

# opening the input file
inputFileStream = open(inputFile)  

# reading the input file and storing the file data into data variable
inputFiledData = inputFileStream.read()                

# Building and initializing the dictionary
dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}    

#Initial string set to NULL
string = ""             # String is null.
compressed_data = []    # variable to store the compressed data.

# iterating through the input symbols.
# LZW Compression algorithm
for symbol in inputFiledData:                     
    string_plus_symbol = string + symbol # get input symbol.

    #Case if input symbol is present in dictionary
    if string_plus_symbol in dictionary: 
        string = string_plus_symbol

    #Case if input symbol is not present in dictionary
    else:
        #Appending dictionary using the new unique string
        compressed_data.append(dictionary[string])

        #Append only if the dictionary size is less than or equal to allotted
        if(len(dictionary) <= maxTableSize):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1

        string = symbol

#Adding the 
if string in dictionary:
    compressed_data.append(dictionary[string])

# storing the compressed string into a file (byte-wise).
out = inputFile.split(".")[0]
output_file = open(out + "_encoded" + ".lzw", "wb")

#Writing compressed contents to the file
for data in compressed_data:
    output_file.write(pack('>H',int(data)))

#Closing file streams
output_file.close()
inputFileStream.close()