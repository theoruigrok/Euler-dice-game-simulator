# This code template is created for Challenge 2: Dice Game. 
# The template must be complete by the student before the submission.

import random as rand
import string
import os

# global variables
# todo 1: std_number must have the correct student number
std_number = '1058308'
#Student name: TJJ Ruigrok van der Werven

# game parameters. Do Not change these variables.
player_one = 'peter'
player_two = 'colin'
test_cases = [ 
    {player_one: {'sides':4,'num':9} , player_two : {'sides':6,'num':6}} ,
    {player_one: {'sides':4,'num':3} , player_two : {'sides':9,'num':2}} , 
    {player_one: {'sides':8,'num':3} , player_two : {'sides':14,'num':1}} , 
    {player_one: {'sides':3,'num':10} , player_two : {'sides':6,'num':1}} , 
    {player_one: {'sides':4,'num':1} , player_two : {'sides':20,'num':1}} 
    ]


def simulate_general_Euler_205(case:dict , num_of_experiments:int = 1_000_000): # Do Not Change this function
    '''
    This function simulates the probability of Dice Game, i.e. Euler 205.
    '''
    def general_dice(sides:int=6): # Do Not Change this function
        '''
        This function implements a general dice function
        '''
        return lambda : rand.randint(1,sides) if sides > 1 else None
    
    def get_dice_collections(): # Do Not Change this function
        '''
        Each player has a collection of dice. This function returns the collections in a dictionary.
        '''    
        dice_peter = general_dice(case[player_one]['sides'])
        dice_colin = general_dice(case[player_two]['sides'])
        return {player_one: [dice_peter]*case[player_one]['num'] , player_two:[dice_colin]*case[player_two]['num']}

    def calculate_probability():
        '''
        This function calculates the probability of winning for one given case.
        '''
        winning_probability = {player_one:0,player_two:0,'Draw':0}
        # todo 2: Complete the implemetation of this function
        # start here ..............
        #initialize parameters for amount of times each player wins, and amount of draws. 
        Peter_wins = 0
        Colin_wins = 0
        draw=0
        #iterate over large number of experiments, and in each iteration, in an inner loop, throw each player's amount of dice. Once all their dice are thrown, 
        #count total dice values for each player, and determine the winner. Increment values for amount of wins for each player, or amount of draws accordingly.
        for exp in range(num_of_experiments):
            #dice face value numbers are reset at the start of each iteration:
            Peter_count = 0
            Colin_count=0
            #number of dice and side count for each player are extracted from the input test cases:
            Peter_sides=case['peter']['sides']
            Colin_sides=case['colin']['sides']
            Peter_N_Dice=case['peter']['num']
            Colin_N_Dice=case['colin']['num']
            #For each player, for number of dice, general_dice() is called, with parameter: side count. It returns a random value for the throw result face value.
            for roll in range(1,Peter_N_Dice+1):
                current_throw=general_dice(Peter_sides)()
                Peter_count+=current_throw
            for roll in range(1,Colin_N_Dice+1):
                current_throw=general_dice(Colin_sides)()
                Colin_count+=current_throw
            #determine winner, which is the highest total dice count:
            if Peter_count>Colin_count:
                Peter_wins+=1
            elif Colin_count>Peter_count:
                Colin_wins+=1
            else:
                draw+=1

        #determine winning probability, by diving by numer of experiments. This is inserted in the dictionary for the initial results of the output
        winning_probability[player_one] = Peter_wins/num_of_experiments
        winning_probability[player_two] = Colin_wins/num_of_experiments
        winning_probability['Draw'] = draw/num_of_experiments

        # finish here ..............       
        return winning_probability # the result of the simulation will be returned here
    return calculate_probability() # do not change this


def find_num_dice_equal_prob(case , max_num_dice=30):
    # probability of the given case will be calculated here
    probs = simulate_general_Euler_205(case)
    message_init_case = 'Initial result for case:'+str(case)+' With Probabilities:'+str(probs)
    fair_case = case
    fair_probs = probs

    # todo 3: complete the function to find a case for a fair game
    # hint: iterate in a loop for max_num_dice and find number of dice for both players such that they play a fair game
    # in each iteration call simulate_general_Euler_205 and check probabilities, increase number of dice for minimum probability, 
    # then call the function again with a new case. 
    # At the end fair_case will contain information of case with updated number of dice and fair_probs will contain probabilities of fair case.

    # start here ..............

    #within range of max number of dice(=30 by default), iterate over increasing number of dice. After each iteration, if winning probabilities for each player are not yet approximately equal,
    #increase number of dice for the player with the lower winning probability, then call function simulate_general_Euler_205() until the winning probabilities are within margin. Once they are in margin, break out of the for loop.
    # Also, in each iteration, the fair_case and fair_probabilites dictionaries are updated with the number of dice and probabilities of the current iteration. This way, when the for loop is broken out of, 
    #assuming that the withinmargin condition is reached eventually, at the end fair_case and Fair_probs will have the correct number of dice and the corresponding probabilities for that number of dice.
    for die in range(1,max_num_dice):
        #withinMargin=the contition that breaks out of the loop. It checks if the probabilities in the current iteration are within 1% of each other.
        withinMargin=abs(fair_probs['peter']-fair_probs['colin'])<0.01
        if fair_probs['peter']<fair_probs['colin'] and not withinMargin:
            fair_case['peter']['num']+=1
            fair_probs=simulate_general_Euler_205(fair_case)
            withinMargin=abs(fair_probs['peter']-fair_probs['colin'])<0.01
            if withinMargin:
                break
        elif fair_probs['colin']<fair_probs['peter'] and not withinMargin:
            fair_case['colin']['num']+=1
            fair_probs=simulate_general_Euler_205(fair_case)
            withinMargin=abs(fair_probs['peter']-fair_probs['colin'])<0.01
            if withinMargin:
                break

    # finish here ..............       
    #here fair_case and fair_probs must be ready with the results of the search    
    message_fair_case = 'Final result for fair game in case:'+str(fair_case)+' With Probabilities:'+str(fair_probs)
    return message_init_case+os.linesep+message_fair_case


def main(): # Do Not change this function
    '''
    This function checks student number, iterates over test cases and stores the final results in a log file.
    '''
    if len(std_number)!=7 or len(set(std_number)-set(string.digits)):
        print('ERROR: student number is not valid')
        return

    log=''
    log_ext = '.txt'
    log_name = 'dice_game_'
    out_file_name = log_name + std_number + log_ext
    # iterate over the test cases
    for case_num in range(0,len(test_cases)):
        log = log + os.linesep*2 + 'CASE '+str(case_num)+os.linesep*2 + find_num_dice_equal_prob(test_cases[case_num])
    # print the result
    print(log)
    # store the result in a log file
    with open(out_file_name,'w') as log_file:
        log_file.write(log)
        log_file.close()
    
main() # Do Not change this function


