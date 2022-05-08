# noledgetech-test Simple translator

## General info
To used this program you have to a Linux operating system and the specified path: '/Users/test/internship/dictionaries',

where should be two files:


- the first named 'PLtoEN.dsv', which contains Polish words and their English equivalent, separated by a delimiter "|",
  
  like:
  
  piłka|ball
  
  słońce|sun

- the second named 'ENtoIT.dsv', which contains English words and their Italian equivalent, separated by a delimiter "|",
  
  like:
  
  ball|palla
  
  sun|sole

## Setup
To starting the program consists launching the file 'noledgetech.py', the program returns on the path a file named 'output.dsv',
which returns the translation of Polish words into Italian.


## Technologies
- Python 3.10

## The scope of functionality
The application startup file contains two functions. Main method "generate_dictionary" takes two paths and use the second function "packet",
which returns a dictionary of these files.
Dictionaries are processed and return the final result in the form of a file.


The program has implemented tests inside another file 'test-noledgetech.py', which include:

- checking the location of files on the path
- checking if the function "packet" returns a dictionary
- checking if the dictionary is not empty
- checking if the main method returns a file
- checking if the returned file is not empty
- checking if the file quantity is consistent with one of the base files
