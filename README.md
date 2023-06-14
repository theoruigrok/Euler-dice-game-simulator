Description: 
This code was developed as the second assignment for the "Analysis" course of the foundation year in the Bachelor of Information Technology program. It is a simulator for the Euler 205 Dice Game. The program applies higher-order functions and combinatorics to simulate the probability of winning the game for different scenarios.

The code includes a simulate_general_Euler_205 function that performs the simulation based on the provided game parameters. It utilizes a general dice function and calculates the probability of winning for each player. The results are returned as a dictionary.

Additionally, the code contains a find_num_dice_equal_prob function that iteratively searches for a fair game scenario by adjusting the number of dice for each player. It calls the simulate_general_Euler_205 function to calculate probabilities and incrementally adjusts the dice count until the probabilities are within a specified margin.

The main function checks the student number, iterates over test cases, and stores the final results in a log file. The log file includes the initial and final results for each test case.

Overall, this code demonstrates the use of higher-order functions and combinatorics to analyze and simulate the probability of winning the Euler 205 Dice Game.

Initially, I attempted to use the itertools module to generate a large set of possibilities and determine the ideal number of dice for each player. However, the calculating time proved to be prohibitive.

To overcome this challenge, I modified my approach and incrementally increased the number of dice for each player, calling the function to check if the resulting probabilities were approximately 50/50. This adjustment significantly reduced the computational overhead while still achieving the requirement of an approximate equal chance of winning.

This assignment not only allowed me to apply higher-order functions and combinatorics but also taught me the importance of adapting my code to meet the project requirements efficiently. It was a valuable learning experience in problem-solving and optimizing code performance.
