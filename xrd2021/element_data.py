"""
This module is a database for element information.
"""
def crystal(ele):
    """
    Tell me the name of element. 
    I will tell you its crystal structure and recorded lattice parameter.
    """
    if ele in ('Cu', 'cu'):
        lat_a = 3.597  # unit is A
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'FCC'  # the name of crystal structure
    if ele in ('Ni', 'ni'):
        lat_a = 3.520  # unit is A
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'FCC'  # the name of crystal structure
    if ele in ('Si', 'si'):
        lat_a = 5.431  # unit is A
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'Diamond_Cubic'  # the name of crystal structure
    if ele in ('Mo', 'mo'):
        lat_a = 3.147  # unit is A
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'BCC'  # the name of crystal structure
    if ele in ('Ti', 'ti'):
        lat_a = 2.951  # unit is A
        lat_b = lat_a
        lat_c = 4.684
        cryst_structure = 'HCP'  # the name of crystal structure
    if ele in ('Al', 'al'):
        lat_a = 4.046  # unit is A
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'FCC'  # the name of crystal structure

    #print("The structure of {} is {}, and lattice parameter is {}.".format(ele, cs, str(a)))

    else:
        lat_a = 0
        lat_b = lat_a
        lat_c = lat_a
        cryst_structure = 'nope'
        print("Our database is so small. It is time to add more element!")

    return cryst_structure, lat_a, lat_b, lat_c
