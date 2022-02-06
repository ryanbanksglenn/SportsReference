# Sports Reference 2022 Internship Application

# Introduction

This Python code accepts head-to-head records from a JSON file and outputs the results in a matrix.  This code was created using the sample JSON in the information about the summer internship position, but it could easily be altered for differing positions.  This code was designed using Python 3.0.  In addition to the standard libraries, the Tabulate library is used.

# Procedure

The code begins by opening the JSON file and creating an array with the list of the teams.  This is the only part of the code that would need to be changed to use the code for other teams.  The length of this array is used to determine the number of teams.

The file then creates the final matrix based on the number of teams.  Next, a while-loop nested inside another while-loop is used to fill the matrix.  The inside while-loop fills in a row of the matrix as the outside while-loop changes the row being filled.  Each matrix entry is filled using the informtion in the JSON file.  The inside while-loop includes an if-statement and an else-statement because of the matrix entries where the same team is on both sides of the matrix.  Since there are no head-to-head results for these locations, the code places "--" for these matrix entries. 

Lastly, the code adds the headings to the matrix and prints the matrix using the tabulate library.
