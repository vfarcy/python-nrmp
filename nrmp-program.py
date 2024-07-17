'''
Author : Miswar
Based On The NRMP Match https://www.youtube.com/watch?v=kvgfgGmemdA
The NRM with Program Proposing First
'''

import collections
import copy

rankApplicant = {
	'Arthur': 	['Projet_02'],
	'Pierre': 	['Projet_02', 'Projet_01'],
	'Joseph':  	['Projet_01', 'Projet_03', 'Projet_02'],
	'Laurent':	['Projet_01', 'Projet_02', 'Projet_03'],
	'Lucie':	['Projet_03', 'Projet_01', 'Projet_02'],
}

rankProgram = {
	'Projet_01': 	['Lucie', 'Joseph'],
	'Projet_02': 	['Lucie', 'Arthur', 'Pierre', 'Laurent','Joseph'],
	'Projet_03': 	['Lucie', 'Arthur', 'Joseph', 'Laurent'],
	
}



positionProgram = {
	'Projet_01'	: 2,
	'Projet_02'	: 5,
	'Projet_03'	: 2,
}



applicantMatchs 	= {}
freeProgram 		= []
checkProgram 	 	=copy.deepcopy(rankProgram)
 

def matching(program):
	'''Find the free applicant available to a program '''
	print("Matching %s"%(program))
	
	rankProgram[program] = list(checkProgram[program])
	
	'''If program not have applicant and slot again, remove from free Program '''

	if(len(rankProgram[program])==0 or positionProgram[program] < 1):
		freeProgram.remove(program)
		print('- Le projet %s n\'a pas de candidat à vérifier ou n\'a plus de place disponible '%(program))
					
	else:
		for applicant in rankProgram[program]:
			
			#Cek whether applicant is taken or not
			if applicantMatchs[applicant] == "":
				if program not in rankApplicant[applicant]:
					print('- Le projet %s n\'est pas demandé par le candidat %s '%(program,applicant))
					checkProgram[program].remove(applicant)
				else:	
					applicantMatchs[applicant]=program
					positionProgram[program]-= 1

					print('- Le projet %s est temporairement affecté au candidat %s '%(program, applicant))
					break
			else:
				print('- Le candidat %s est provisoirement affecté au projet %s '%(applicant,applicantMatchs[applicant]))

				if program not in rankApplicant[applicant]:
					print('- Le projet %s n\'est pas demandé par le candidat %s '%(program,applicant))
					checkProgram[program].remove(applicant)

				else :
					# get program who can remove, 
					if rankApplicant[applicant].index(applicantMatchs[applicant]) < rankApplicant[applicant].index(program): 
						print('- Le classement du projet %s pour le candidat %s est supérieur au projet actuel %s  '%(program,applicant,applicantMatchs[applicant]))
						checkProgram[program].remove(applicant)
					else:
						print('- Le projet %s correspont mieux que le projet %s'%(program, applicantMatchs[applicant]))
						print('- Nouvelle déaffectation du projet %s .. et affectation provisoire du projet %s au candidat %s'%(applicantMatchs[applicant], program, applicant))

						#The old program is now not match anymore
						positionProgram[applicantMatchs[applicant]] += 1
						checkProgram[applicantMatchs[applicant]].remove(applicant)
						freeProgram.append(applicantMatchs[applicant])
						
						#The new applicant have match 
						applicantMatchs[applicant]=program
						positionProgram[program]-=1
						
						break

			

# init all applicant free and not have program
for program in rankProgram.keys():
	freeProgram.append(program)

# init applicantMatchs
for applicant in rankApplicant.keys():
	applicantMatchs[applicant]=""

# Matching algorithm until stable match terminates
i=1
while (len(freeProgram) > 0 ):
	for program in freeProgram:
		matching(program)
		i=i+1
		

print("\nMatching Done\n",applicantMatchs)

