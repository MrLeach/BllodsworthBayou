# BllodsworthBayou
GCSE Python Project

This is some code to get students started. Here is the basic idea...

Each person has their own python file which contains the logic for moving between the locations, and also contains your own version of the fighting algorithm.

Different people in your group will write the code for different locations. Each person will do that in a cunningly named file which the rest of the group can import. That way, you can share each other's code and complete the game.

A side effect of this is that if one person commits a file which is broken, all the people in the group will find their code coean't work! No Pressure..... 

For example, if the group contains Alice, Bob and Carol

bob.py - this will be the python file that bob uses. It will be a copy of the code in 'myname.py' which will also contain bob's fighting algorithm.

bob_lib.py - this will be the functions which bob writes for the locations which he is doing. It will be imported into everyone else's files with the 'from bob_lib import *' line.

Bob will work on the code for the locations and test them. When he is happy with his changes he will ADD the file to the list of changed files, then he will COMMIT the new version to his local version of the repository, then he will PUSH the bob_lib file up to GIT. Other members of the group can then PULL the changes down to their copies of the repository.
 
