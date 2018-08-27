-------Author-----
Naitik Dodia - 201501177
Kaushal Patel - 201501219

------------------

This file contains the information about how to run the code for the simulation.

--------ver5.py---------

Line 57 contains the loop which varies a statistic of the model.
These variable statistics are present between the lines 35 and 50.
fp = variable set of fire probabilities
sp = variable set of survival probabilities
pv = variable set of initial fraction of vegetations

fireprob = constant set of fire probabilities
survivalprob = constant set of survival probabilities
pveg = constant set of initial vegetation ratios

To run for each statistic change the parameters of the for loop in the line 57 as follows:

for <constantSet_name> in <variableSet_name>

Line 216, 217, 141 and 142 contain code for displaying the simulation of the model. Uncomment these lines to watch the simulation:

After run Figure 1 corresponds to the vegetation in the order mentioned in the report.
Figure 2 corresponds to the age of Juvenile vegetation and 0 in this figure corresponds to not Juvenile vegetation
Figure 3 corresponds to the state of the vegetation in the order [Burnt = 0, Burning = 1, Unburnt = 2]


-------ver3.py-------
This is skeleton code for ver5.py and any direct simulation can be run using this file by changing the values of variables mentioned in the above description.