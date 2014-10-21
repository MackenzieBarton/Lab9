############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
print list2



keepGoing = True


while (keepGoing == True):
    print 'What is your temperature?'
    temp = int(raw_input())
    print 'Have you been to West Africa recently(yes - 1 or no - 2)?'
    africa = int(raw_input())
    print 'Have you been sick in the last 24 hours(yes - 1 or no - 2)?'
    sickness = int(raw_input())
    print 'Are there any more patients(yes - 1 or no - 2)?'
    patient = int(raw_input())
    if temp > 105:
        print 'You need to go to the hospital'
    elif africa == 1 + temp > 102:
        print 'You need to go to the hospital'
    elif temp > 100 or sickness == 1 + africa == 1:
        print 'You need to go to the hospital'
    else:
        print 'You are fine and can stay home'
    if patient == 1:
        keepGoing = True
    else:
        keepGoing = False
