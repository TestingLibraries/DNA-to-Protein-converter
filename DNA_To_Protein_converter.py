## This starting segment is to convert the antisense/template strand to mRNA.

User_DNA = input("Input your template/antisense DNA in the format 5'XXX3' or 3'XXX5' ")

RNA_Polymerase = {           "5" : "3",
                             "A" : "U",
                             "T" : "A",
                             "G" : "C",
                             "C" : "G",
                             "'" : "'",
                             "3" : "5"
}

mRNA = ""
for Template_Base_Pair in User_DNA :
    mRNA_base_Pair = RNA_Polymerase[Template_Base_Pair]
    mRNA += mRNA_base_Pair

## Code to display 3'XXX5' mRNA in 5'XXX3' format
if mRNA.startswith("3") :
    # Flip the sequence backwards. 
    mRNA = mRNA[::-1]
    # but now we will get '5XXX'3, which we dont want, we want 5'XXX3' 
    # Lets strip off '5 and '3, and then concatenate 5', the stripped mRNA, and 3'
    mRNA = (f"5'{mRNA[2:-2]}3'")
    print("Your mRNA sequence is ",mRNA)

else :
    print("Your mRNA sequence is ",mRNA)

### Now, for future key:value pairing, lets take out the 5' and 3' we added
mRNA = mRNA[2:-2]

## This second segment converts mRNA to a primary protein structure

### First, lets declare our dictionary. This dictionary is for converting between amino acids and codons
Ribosome = {}

### Now i declare a function which will allow me to type out one amino acid for multiple codons, in a tuple. 
def add_codon(amino_acid , codon_list) :
   ### Now i need another function which will allow me to cycle through the individual codons in my codon_list tuple
   for codon in codon_list :
    ### After cycling through each codon, i need to pair this codon with the amino acid in a key value pair, and add it to the dictionary both at once.
        Ribosome[codon] = amino_acid

### Now lets use our function to declare amino acid and codon lists, and cycle through each codon list to add codon : amino acids pairs to our dictionary
add_codon("Phe-" , ["UUU" , "UUC"])
add_codon("Leu-" , ["UUA" , "UUG" , "CUU" , "CUC" , "CUA" , "CUG"])
add_codon("Ile-" , ["AUU","AUC","AUA"])
add_codon("Val-" , ["GUU" , "GUC" , "GUA" , "GUG"])
add_codon("Ser-" , ["UCU" , "UCC" , "UCA" , "UCG" ,"AGU", "AGC"])
add_codon("Pro-", ["CCU","CCC","CCA","CCG"])
add_codon("Thr-", ["ACU","ACC","ACA","ACG"])
add_codon("Ala-" , ["GCU","GCC","GCA","GCG"])
add_codon("Tyr-" , ["UAU","UAC"])
add_codon("" , ["UAA","UAG" ,"UGA"])
add_codon("His-" , ["CAU","CAC"])
add_codon("Gln-" , ["CAA","CAG"])
add_codon("Asn-" , ["AAU", "AAC"])
add_codon("Lys-" , ["AAA","AAG"])
add_codon("Asp-" , ["GAU" , "GAC"])
add_codon("Glu-" , ["GAA" , "GAG"])
add_codon("Cys-" , ["UGU" , "UGC"])
Ribosome["UGG"] = "Trp-"
add_codon("Arg-" , ["CGU" ,"CGC" ,"CGA" , "CGG" ,"AGA", "AGG"])
add_codon("Gly-" , ["GGU" ,"GGC" ,"GGA","GGG"])

### Just for fun, here is the start codon without the add_codon function, as you can see, the previous functions simply loop through the codon list
### and then pair the codons in the list to the amino acid, using the below mentioned syntax, before moving on to the next codon
Ribosome["AUG"] = "Met-"


## Now lets start converting our mRNA into a protein.

### Lets declare some useful variables 

length_of_mRNA = len(mRNA)
### This is the initial position from which we will search for AUG. 
### Since we intend to scan the entire length of the DNA for AUG, we will start from zero, and increment by 1
start_point = 0
### For now, we will assume that there are no end and start points
### This will provide me with an easy way to display error messages like "This start point lacks an end point"
End_Point_present = False
Start_Codon_Exists = False

while start_point < length_of_mRNA :

    ## Check if there is a start codon present
    ## if not, restart the loop
    if mRNA[start_point:start_point+3] == "AUG" :

        print("There is a start point at position",start_point)
        ## Flip our variable to true, so that we avoid displaying an error message later
        Start_Codon_Exists = True
        ## loop and check if this start point has an end point in the same reading frame
        for end_point in range(start_point,length_of_mRNA,3) :
            if mRNA[end_point:end_point+3] in ["UAA","UAG","UGA"] :
            ## no stop codon before reading whole sequence --> resume for loop
            ## no stop codon after reading whole sequence --> jump to "End point present"
                print("This start point has an end point at",end_point)
                End_Point_present = True
                ## Lets convert our sequence into a protein
                protein = ""
                for base_pair in range(start_point,end_point,3) :
                ## lets extract our codon
                    mRNA_Codon = mRNA[base_pair:base_pair+3:1]
                ## lets input this codon into our ribosome
                    Amino_Acid = Ribosome[mRNA_Codon]
                ## lets add this Amino acid to our protein chain
                    protein += Amino_Acid
                ## Lets bind Nitrogen and Carboxyl to our Protein
                protein = (f"N-{protein}C")

                ## Lets print our protein
                print("For this set of start and stop codons, your protein is ", protein)
                
        ## If there was no end point present in the whole reading frame for a particular start codon
        if End_Point_present == False :
            print("This start codon has no stop codon, moving on")
        ## If there was an end point present, flip the variable back to false
        ## This way the error message can still be displayed even if a previous start codon had an end codon
        if End_Point_present == True :
            End_Point_present = False
    ## once we have finished checking if the start point had an end point
    ## lets resume the while loop from the next base pair
    start_point += 1

## Once we have finished scanning the entire DNA, two things can happen
## Either there was no start codons, in which case we will display this message
if Start_Codon_Exists == False :
    print("There are no start codons in this entire sequence")
    quit()
## Or, there was indeed a start codon, in which case we simply quit
print("DNA scan complete, shuting down....")
quit()