'''
Created on Apr 25, 2022
Description:This code asks someone how any items they want. each item has on food item from each list, there are 3 list. 
no item can have the same food items meaning the maximum amount variations that can be made is 15, 
because there's only 15 items in each list.
@author: athompson23
Plan: ask how many items they want and then print it
Bugs: none
bonus: enhanced listing features, random price, no repeating list items, has a response for all answers to initial question.

'''
import random


def main():

    
    list_1 = ['local ', 'roasted ', 'grilled ', 'garlic mashed ', 'oven dried ', 'spiced ', 'stewed ', 'assorted ', 'iced ', 'sliced ', 'braised ', 'free-range ', 'baby ', 'yaki glazed ', 'steamed ']
    list_2 = ['cauliflower ', 'tilapia fillet ', 'pork loin ', 'green beans ', 'basmati rice ', 'rainbow carrots ', 'fingerling ', 'potatoes ', 'three color squash ', 'potatoes ', 'eggplant ', 'drumstick ', 'short rib ', 'duck breast ', 'eye round of beef ', 'baguette ']
    list_3 = ['with fennel', 'gratin', 'bengali style', 'with peas', 'pizza', 'with balsamico', 'with garlic and olive oil', 'with pigeon peas', 'with minted yogurt', 'soup', 'chutney', 'salad', 'with tropical fruit salsa', 'over sticky rice', 'au jus']
    list_4 = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
    counter = 0                                                         #controls the number of loops
    number = 1                                                          #accumulator the printer number
    try:
        question = int(input("how many items do you want?\n"))
        
    #different outcomes for question
        if question > 15:                                               #elif for invalid answer to question
            print ("the max number of items is 15")
            return main()
        elif question == 0:                                             #elif for invalid answer to question
            print ("Good bye then.")
        elif question < 0:                                              #elif for invalid answer to question
            print ("enter a number 1-15")
            return main()
        elif question <= 15:                                            #elif for invalid answer to question
            while counter < question:           
                RL1 = (random.choice(list_1))                           #random selects item from list 1
                RL2 = (random.choice(list_2))                           #random selects item from list 2
                RL3 = (random.choice(list_3))                           #random selects item from list 3
                print  ("%d. " % (number) + (RL1) + (RL2) + (RL3))
                
                list_1.remove(RL1)                                      #removes used item from list 1 before it loops
                list_2.remove(RL2)                                      #removes used item from list 1 before it loops
                list_3.remove(RL3)                                      #removes used item from list 1 before it loops
                counter += 1                                            #adds 1 to counter before it loops again
                number += 1 
            
            #print(pos_list_4)
        if counter == question:    
            price = random.randint(5,15)
            final_price = str(price*question)   
            #final_price = question*6                               #ends the loop when when the correct amount of loops have been made
            print ("your final price is $" + final_price + ".")
            print ("")                                              #adds a line between the final price the question being asked again
            return main()
        
            
    except:                                              #if someone answer the question with words instead of number it gives them this prompt and asked again
        print ("please print a number 1-15")
        return main()


if __name__ == '__main__':
    main()            
