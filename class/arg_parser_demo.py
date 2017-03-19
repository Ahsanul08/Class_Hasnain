# First import the module

import argparse

# Initialize argument parser

parser = argparse.ArgumentParser()


# Call the method

#parser.parse_args()


# Add a positional argument

parser.add_argument("first")
parser.add_argument("second")
parser.add_argument("third")

#args = parser.parse_args()

# Access the argument

#print args.first

#Add a help message

#parser.add_argument("first", help = "Print the string you give")

#args = parser.parse_args()

#print args.first

# define the type of argument 

#parser.add_argument("square", help = "Output the square of the given number", type = int)

#args = parser.parse_args()

#print args.square ** 2 


# Add a positional argument

#parser.add_argument("--second", help = "Show the help message.")


#parser.add_argument("--optional", help = "Show the output in detail", action = "store_true")

# Add the shorter version

#parser.add_argument("-o", "--optional", help = "Show the output in detail", 
#			action= "store_true")


#parser.add_argument("--optional", help="Print the number if matches with choice",choices=[0,1,2], type= int)

#parser.add_argument("-v","--verbose", help= "Show verbose message", action= "count")

args = parser.parse_args()

print len(vars(args))



#if args.verbose:
#    if args.verbose == 1:
#        print("lowercase message")
#    elif args.verbose == 2:
#        print("UPPERCASE MESSAGE") 
