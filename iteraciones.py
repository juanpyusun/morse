 import itertools

 mylist = [1, 2, 3, 4]# this is the list from which to draw the subsets

 print (mylist)# the first subsequence of the list is the list itself
 # iterating through the possible numbers of commas to be distributed
 for n in range(1, len(mylist)):
     comma_positions_comb = list( itertools.combinations(range(1,len(mylist)), n) )
     # iterating through the combinations of comma positions
     for comma_positions in comma_positions_comb:
         subset = []
         start_id = 0
         # iterating through the specific comma positions in the given combination
         for single_comma_position in comma_positions:
             subset.append(mylist[start_id:single_comma_position])
             start_id = single_comma_position
         # the last bit of the list must be appended by hand
         subset.append(mylist[start_id:])
         print (subset)

