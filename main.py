import re

## BUGS
## 1. max() only does first maximum value if duplicates exist.
## 2. 

## TO COME LATER - Ask user for input file. Note that input file must
## be in Clustal format w/ numbers. (maybe without numbers too?)


## Ask user for section size. Ask user to name output file.
## TO COME LATER - verify that input is an integer between x and y.

print('\n')
sectionsize = int(input('Enter the desired section size (Recommended value: 250): '))
print('\n')
output_name = input('Enter a name for the output file: ')

## Make the complete match/mismach sequence, including only the match/mismatch line 
## while also cutting out the blank space that comes before the actual match/mismach
## data.

totalseq = '' 
gt11 = ''
gt12 = ''
gt31 = ''
gt41 = ''


# Match/Mismatch
i=0
j=0
with open('HEV_alignment_main.txt') as f:
	for line in f:
		i=i+1
		j=i-2
		if j%6==0 and j>0:
			line=line[17:77]
			totalseq=totalseq+line

# Genotype 1-1
i=0
j=0
with open('HEV_alignment_main.txt') as f:
	for line in f:
		i=i+1
		j=i
		if j%6==0 and j>0:
			line=line[17:77]
			gt11=gt11+line
		#last_line = f.readlines()[-1]

# Genotype 1-2
i=0
j=0
with open('HEV_alignment_main.txt') as f:
	for line in f:
		i=i+1
		j=i-1
		if j%6==0 and j>0:
			line=line[17:77]
			gt12=gt12+line

# Genotype 3-1
i=0
j=0
with open('HEV_alignment_main.txt') as f:
	for line in f:
		i=i+1
		j=i+1
		if j%6==0 and j>0:
			line=line[17:77]
			gt31=gt31+line
			
# Genotype 4-1
i=0
j=0
with open('HEV_alignment_main.txt') as f:
	for line in f:
		i=i+1
		j=i+2
		if j%6==0 and j>0:
			line=line[17:77]
			gt41=gt41+line
					

print('\n')
print('Match/Mismatch')
print(len(totalseq))
#print(totalseq)

print('\n')
print('Sequence 1-1')
print(len(gt11))
#print(gt11)

print('\n')
print('Sequence 1-2')
print(len(gt12))
#print(gt12)

print('\n')
print('Sequence 3-1')
print(len(gt31))
#print(gt31)

print('\n')
print('Sequence 4-1')
print(len(gt41))
#print(gt41)

print('\n')			
print('The alignment matches are shown below. Matches are represented with \
a "*" and  mismatches with a blank space. \n')
print(totalseq)
print('\n')

print('The length of the string is: ' + str(len(totalseq)))

## Count the number of matches per section for the length of the sequence minus
## the section size. Afterwards, print the index (nucleotide) of the max number
## of matches and the amount of matches.

i=0
matches_per_section = []
while i <= len(totalseq)-sectionsize:
	i=i+1
	#print(i)
	section=totalseq[i:i+sectionsize]
	#print(section)
	#print('The section is from nucleotide ' + str(i) + ' to nucleotide ' \
	#	+  str((i+sectionsize)-1) + '.')
	#print('The length of the section is ' + str(len(section)) + ' nucleotides.')
	#print('The percent of nucleotides matching is ' + \
	#	str(section.count('*')/sectionsize*100) +'%.')
	#
	matches_per_section.append(section.count('*'))
	#print('\n')
	#print(matches_per_section)

#print(matches_per_section)
loc_most_matches = matches_per_section.index(max(matches_per_section))

print('\n')
print('The starting location of the section with the highest number of matches is ' + \
	str(loc_most_matches+1) + '.')
print('\n')
print('The number of matches in that section is ' + \
	str(matches_per_section[matches_per_section.index(max(matches_per_section))]) \
	+ ' (' + str(matches_per_section[matches_per_section.index(max(matches_per_section))]/sectionsize*100) \
	+	'%). ')
print('\n')


## Find the actual sequence corresponding to the section with the highest number of matches.

gt11_most_matches = gt11[loc_most_matches:loc_most_matches+sectionsize]
print(len(gt11_most_matches))
print(gt11_most_matches)

with open(output_name+'.txt','w') as f:
	f.write(gt11_most_matches)
	f.close()
	
