"""
Created on sept 8, 2022
This code is used for helping the post office become more automated, all someone has to do
is enter the information correctly, and they will be told; the type of mail they're sending
and how much it will cost the cost is a combination of what type of mail it is plus how far
the mail will travel
sample data: (10, 12, 20, 21505, 72400), (1, .12, .3, 21500, 0004)
version 1.2(10/3/2022): turned assigning mail type and formatting price into functions, also added while loop so code
runs 5 times
@author: AThompson23
"""
from termcolor import colored
# function that assigns the starting and ending location of the mail
def getzip(zip):  # zip is either sender or location and puts out s_zone or e_zone respectively

    if 1 <= zip <= 6999:
        return 1  # return 1 to the variable s_zone or e_zone
        # zone 2
    elif 7000 <= zip <= 19999:
        return 2  # return 2 to the variable s_zone or e_zone
        # zone 3
    elif 20000 <= zip <= 35999:
        return 3  # return 3 to the variable s_zone or e_zone
        # zone 4
    elif 36000 <= zip <= 62999:
        return 4  # return 4 to the variable s_zone or e_zone
        # zone 5
    elif 63000 <= zip <= 84999:
        return 5  # return 5 to the variable s_zone or e_zone
        # zone 6
    elif 85999 <= zip <= 99999:
        return 6  # return 6 to the variable s_zone or e_zone
    else:
        print("UNMAILABLE.")
        return main()
# function that assigns type of mail
def gettype(length, height, thickness, f_zone, p_class):
    if 6 >= height >= 3.5 <= length <= 4.25 and .007 <= thickness <= .016:

        final_price = .20 + (.030 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # large post card
    elif 11.5 >= height > 6 >= length > 4.25 and .007 < thickness <= .015:

        final_price = .37 + (.030 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # normal envelope
    elif 5 <= height <= 11.5 and 3.5 <= length <= 6.125 and .016 <= thickness <= .25:

        final_price = .37 + (.040 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # large envelope
    elif 11 <= height <= 18 and 6.125 < length <= 24 and .25 < thickness <= .5:

        final_price = .60 + (.050 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # package class
    elif p_class > 130:
        print(colored("UNMAILABLE.", 'grey', 'on_red'))
        return main()  # shoots you back to the beginning
    elif 67 < p_class <= 84:  # and thickness > .5 and height > 18 and length > 24:
       
        final_price = 2.95 + (.250 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # large package class
    elif 84 < p_class <= 130:  # and thickness > .5 and height > 18 and length > 24:
        # print(colored("you have a large package",'white'))
        final_price = 3.95 + (.350 * f_zone)  # takes F_zone and multiples it with the price per zones travelled
        return final_price
    # if something other than accepted dimensions are given
    else:
        print(colored("UNMAILABLE.", 'grey', 'on_red'))
        return main()  # shoots you back to the beginning
# function that formats final price
def getprice(final_price):
    try:  # all of this is for formatting the final price
        if final_price[0] == '0' and final_price[3] == "0":  # if the 1st digit is a 0 and the 4th digit is a zero,
            # it deletes the 1st 0
            final_price = final_price[:0] + final_price[1:]
            return final_price
        elif final_price[:1] == "0":  # if the 1st digit is a 0 and the 4th digit is not a zero, it deletes the 1st 0
            final_price = final_price[:0] + final_price[1:]
            return final_price
        elif final_price[3] == '0':  # if the 1st digit is not a 0 and the 4th digit is a zero, it prints that number
            return final_price
        elif final_price[
            3] != '0':  # if the 1st digit is not a 0 and the 4th digit is not a zero, it prints that number
            return final_price
        else:  # if the 1st digit is not a 0 and the 4th digit is not a zero, it prints that number + a 0 on
            # the end
            final_price = (final_price + "0")
            return final_price
    except:  # if there is no 3rd digit
        if final_price[:1] == "0":  # if there is no 3rd digit and the 1st digit is 0, it deletes the 1st 0 and adds
            # another 0 the end
            final_price = (final_price[:0] + final_price[1:] + '0')
            return final_price
        else:  # if there is no 3rd digit and the 1st digit is not a 0, it adds another 0 the end
            final_price = (final_price + "0")
            return final_price
# main code function
def main():
    final_price = float(0)  # the final price of the mails being sent
    s_zone = float(0)  # the area code of where the mail is being sent from
    e_zone = float(0)  # the area code of where the mail is being sent to
    f_zone = float(0)  # the number of zones the mail will be crossing
    extra = float(0)
    loop = 1
    # initial input
    try:
        if loop <= 5:
            while loop <= 5:
                info = input("Sate information\n")  # starting question
                x = info.split(",")  # splits input by ","
                length = float(x[0])  # takes first data point and sets it to length
                height = float(x[1])  # takes second data point and sets it to height
                thickness = float(x[2])  # takes third data point and sets it to thickness
                sender = float(x[3])  # takes fifth data point and sets it to sender
                location = float(x[4])  # takes sixth data point and sets it to location
                s_zone = getzip(sender)  # sends sender variable into function
                e_zone = getzip(location)  # sends location variable into function
                f_zone = abs(s_zone - e_zone)  # quick calculation which finds the number of zones travelled
                p_class = (((height + thickness) * 2) + length)
                final_price = gettype(length, height, thickness, f_zone,
                                      p_class)  # calls function to assign type of mail
                final_price = str(final_price)  # converts currency into string
                final_price = getprice(final_price)
                print(final_price)
                loop = loop + 1
        elif loop == 6:
            exit()
    except:  # if something is given in the original input that is not excepted this tells you to try again
        print(colored("UNMAILABLE.", 'grey', 'on_blue'))
        return main()
if __name__ == '__main__':
    main()
