#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class element():
    """
    This function is to give some often-used property of elements.
    For now, it can provide lattice parameter, crystal structure.
    """
    def crystal(ele):
        """
        This method is to give the structure information.
        """
        if ele == 'Cu' or 'cu':
            a=3.597   #unit is A
            cs = 'FCC'   #the name of crystal structure
            print("The structure of {} is {}, and lattice parameter is {}.".format(ele, cs, str(a)))
        else:
            a=0
            cs = 'nope'
            print("Our database is so small. It is time to add more element!")
        return cs,a
    
    def energy(ele):
        """
        This function is to provide the charcteristic energy value.
        """
        e = 3  #unit is eV
        return e

