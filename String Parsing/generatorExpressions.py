
import parts

# Part a. Names of suppliers that supply bolts
boltsupps = set(s[1] for s in parts.suppliers for i in parts.spj for p in parts.parts if s[0] in i if i[1] in p if p[1]=='Bolt')
print boltsupps

# Part b. Names of suppliers that supply red parts
redsupps = set(s[1] for s in parts.suppliers for i in parts.spj for p in parts.parts if s[0] in i if i[1] in p if p[2]=='Red')
print redsupps

# Part c. Pairs of names of suppliers that are located in the same city.
pairs = set(tuple(j[1] for j in parts.suppliers if s[3]==j[3]) for s in parts.suppliers for r in parts.suppliers if (s[3]==r[3]) and (s[0] != r[0]))
print pairs

# Pre-reduction code. Probably easier to understand.
'''# Part a. Names of suppliers that supply bolts
bolts = set(j[0] for j in parts.parts if j[1]=='Bolt')
boltsuppids = set(r[0] for r in parts.spj if r[1] in bolts)
boltsupps = set(s[1] for s in parts.suppliers if s[0] in boltsuppids)

print boltsupps


# Part b. Names of suppliers that supply red parts
redparts = set(j[0] for j in parts.parts if j[2]=='Red')
redsuppids = set(r[0] for r in parts.spj if r[1] in redparts)
redsupps = set(s[1] for s in parts.suppliers if s[0] in redsuppids)

print redsupps


# Part c. Pairs of names of suppliers that are located in the same city.

cities = set(s[3] for s in parts.suppliers for r in parts.suppliers if (s[3]==r[3]) and (s[0] != r[0]))
# Used tuple rather than frozenset for clearer output.
pairs = set(tuple(j[1] for j in parts.suppliers if i==j[3]) for i in cities)

print pairs'''