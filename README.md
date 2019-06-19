# Bin_Packing

Seeking to pack n integers into bins of fixed capacity, using the minimal number of bins possible, the One Dimensional Minimum Bin Packing Problem (BPP) is an NP-Hard problem. The Evolutionary Algorithm (EA) seeks a candidate solution for BPP. In attempts to find a candidate solution for BPP the EA uses mutation, a round robin selection, strings of floating point values as chromosomes, and parameters. Depending on the combination of the parameters, the behavior of the EA can greatly change.

To use this program compile the bin packing file and provide a file of numbers (see data file in repo) with the -f argument. A user can also change the mutation rate, -m option, population size, -p option, generation size, -g option, bin capacity size, -c option, the constant size (used for fitness), -k option, the survial rate with the -s option, have the program display more details with the -d option, and have the output write to a file with the -o option.
Example:
python bin_packing.py -f ..\\data\\500numbers.dat -c 100 -p 100 -o dataset500


This project was created for a Evolutionary Computation class at St. Cloud State University in collaborations with Ben Jacobs.
