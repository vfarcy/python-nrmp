'''
Author : Miswar
Based On The NRMP Match https://www.youtube.com/watch?v=kvgfgGmemdA
The NRM with Applicant Proposing First
'''

import collections
import copy

rankApplicant = {
	'Arthur': 	['Projet_02'],
	'Pierre': 	['Projet_02', 'Projet_01'],
	'Joseph':  	['Projet_02', 'Projet_03', 'Projet_01'],
	'Laurent':	['Projet_01', 'Projet_02', 'Projet_03'],
	'Lucie':	['Projet_02', 'Projet_01', 'Projet_03'],
}

rankProgram = {
	'Projet_01': 	['Lucie', 'Joseph'],
	'Projet_02': 	['Lucie', 'Arthur', 'Pierre', 'Laurent','Joseph'],
	'Projet_03': 	['Lucie', 'Arthur', 'Joseph', 'Laurent'],
	
}

positionProgram = {
	'Projet_01'	: 2,
	'Projet_02'	: 2,
	'Projet_03'	: 2,
}

programMatchs 	= {}
freeApplicant 	= []
checkApplicant  =copy.deepcopy(rankApplicant)

def matching(applicant):
	'''Find the free program available to a applicant '''
	print("Matching %s"%(applicant))

	rankApplicant[applicant] = list(checkApplicant[applicant])

	'''If Applicant not have program again, remove from free Applicant '''
	if(len(rankApplicant[applicant])==0):
		freeApplicant.remove(applicant)
		print('- Le candidat %s n\'a pas de projet à vérifier de nouveau ' %(applicant))
					
	else:
		for program in rankApplicant[applicant]:
			
			#Cek whether program is full or not
			if len(programMatchs[program]) < positionProgram[program]:
				if applicant not in rankProgram[program]:
					print('- Le candidat %s n\'est pas elligible au projet %s '%(applicant,program))
					checkApplicant[applicant].remove(program)
				else:	
					programMatchs[program].append(applicant)
					freeApplicant.remove(applicant)
					print('- %s n\'est plus un candidat libre et bénéficie désormais provisoirement du projet %s'%(applicant, program))
					break
			else:
				print('- Le projet %s est complet (%s participant(s)) '%(program,positionProgram[program]))

				if applicant not in rankProgram[program]:
					print('- Le candidat %s n\'existe pas dans la liste des candidats au projet %s '%(applicant,program))
					checkApplicant[applicant].remove(program)
				else :
					# get applicant who can remove, 
					applicantRemove = applicant
					for applicantMatch in programMatchs[program]:
						if rankProgram[program].index(applicantRemove) < rankProgram[program].index(applicantMatch): 
							applicantRemove = applicantMatch

					if applicantRemove==applicant:
						print('- Le classement du candidat %s pour le projet %s is moins bon que les candidats actuellement affectés '%(applicant,program))
						checkApplicant[applicant].remove(program)
					else:
						print('- %s est mieux classé que %s'%(applicant, applicantRemove))
						print('- Déaffectation de %s .. et affectation provisoire du candidat %s au projet %s'%(applicantRemove, applicant, program))

						#The new applicant have match 
						freeApplicant.remove(applicant)
						programMatchs[program].append(applicant)

						#The old applicant is now not match anymore
						freeApplicant.append(applicantRemove)
						programMatchs[program].remove(applicantRemove)

						break

			

# init all applicant free and not have program
for applicant in rankApplicant.keys():
	freeApplicant.append(applicant)

# init programMatch
for program in rankProgram.keys():
	programMatchs[program]=[]

# Matching algorithm until stable match terminates
while (len(freeApplicant) > 0):
	for applicant in freeApplicant:
		matching(applicant)

print("\nMatching Done\n",programMatchs)

