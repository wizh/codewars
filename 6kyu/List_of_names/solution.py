def namelist(s):
    return (''.join((i != 0) * ' ' +  '& ' + n['name'] if i == len(s) -1 
                                                       else ', ' + n['name']
                                                       for i, n in
						  							   enumerate(s))[2:])
