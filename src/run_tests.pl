#!/usr/bin/perl
use strict;
use warnings;

for (my $i=0; $i <= 29; $i++) {
   system("python bin_packing.py -f ..\\data\\500numbers.dat -c 100 -p 100 -o dataset500_$i");
}