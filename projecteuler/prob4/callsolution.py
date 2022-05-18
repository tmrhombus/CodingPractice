import solution as sol
import ndigitsol as nd


#i,j,themax = sol.solution()
#
#print("Largest 3x3-digit palendrome is {} x {} = {}".format(i,j,themax))

idig = 3
jdig = 3

i,j,themax = nd.solution( idig, jdig )

print("Largest {}x{}-digit palendrome is {} x {} = {}".format(idig, jdig, i, j, themax))


