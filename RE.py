import re

def isEmail(inp):


    #email=('benashigbui@gmail.com')
    #email1=('ben$ashigbui@gmail.com')



    #result = re.search ('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',inp)
    result = re.match ('\w+@\w[.]\com',inp)
    if result == None:

        return False

    else:

        return True

    print isEmail('benashigbui@gmail.com')

    print

    print isEmail('ben$ashigbui@gmail.com')

    print



def Txt(extentions):

    return re.search(r'\s\w\.\txt$\s', extentions)

    #return re.search('.*\.txt$',extentions)

    print getTxts('sal.txt mey.ppt ben.html nana.txt kwame.txt akos.txt b33ma.doc')




def percAwesome(inp):

    result = re.search (r'(AWESOME|AWES0ME)',inp)

    if result ==    None:

            return False

    return result.groug(1)



    print percAwesome ('i am AWESOME and AWES0ME is 1 so AWES0ME')

        

