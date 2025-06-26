# DNA-to-Protein-converter
A python program that can convert genomic DNA to proteins

## How do i use this program?

- simply download and start the DNA_To_Protein_converter.py
- Enter/paste a template/antisense strand in the following format 5'XXX3' or 3'XXX5'

## I need some sample DNA, can you give me some sequences?

Sure! here are some sequences for you

### This sequence should yield a few proteins
5'ATGTTTCGCATCACCAACATTGAGTTTCTTCCCGAATACCGACAAAAGGAGTCCAGGGAATTTCTTTCAGTGTCACGGACTGTGCAGCAAGTGATAAACCTGGTTTATACAACATCTGCCTTCTCCAAATTTTATGAGCAGTCTGTTGTTGCAGATGTCAGCAACAACAAAGGCGGCCTCCTTGTCCACTTTTGGATTGTTTTTGTCATGCCACGTGCCAAAGGCCACATCTTCTGTGAAGACTGTGTTGCCGCCATCTTGAAGGACTCCATCCAGACAAGCATCATAAACCGGACCTCTGTGGGGAGCTTGCAGGGACTGGCTGTGGACATGGACTCTGTGGTACTAAATGAAGTCCTGGGGCTGACTCTCATTGTCTGGATTGACTGA3'

### This sequence should give an error, no start sites
5'AAAAAAAAAAAAAAAA3' 

### This sequence Should give one start site that has a stop site, and one start site that lacks a stop site
3'TACCGCATAATACGGGTTTATTCCC5'

## What are the capabilities of this program?

- it can convert DNA to protein for you 
- Finds stop sites that are within the reading frame of the start site AUG
- Can convert multiple start sites and stop sites on the same mRNA to their own protein sequences
- This program does not stop at one gene per DNA sequence, it scans for all the start and stop sites and shows their protein sequences

## Can you summarize this program for me?
Okay!
1. Convert DNA to mRNA using a dictionary
2. scan that mRNA for 5'AUG3'
3. if no 5'AUG3' present, display an error message and shut down.
4. if 5'AUG3' present, check if a stop codon exists within the same reading frame in the mRNA
5. if no stop codon present, display an error, resume scanning the rest of the DNA for the next 5'AUG3'
6. if the next 5'AUG3' has a stop codon within the same reading frame,
7. convert the sequence between the 5'AUG3' and stop codon into a protein
8. print and display the protein to you
9. Move on to the next 5"AUG3' until the entire DNA sequence has been scanned

## What dependencies do i need to run this?
Nothing! this thing is stock python.

