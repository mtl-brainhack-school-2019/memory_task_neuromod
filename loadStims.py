
import os
import random

#Creates a class object (a matrix) listing all image paths in a list according to their subcategory
##Each list is also listed in a bigger list corresponding to the broader semantic category
class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return sorted(filePathlist)
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))


def loadStims():
    maindirs = os.listdir(os.getcwd())
    categories = [Category(maindir).categCreate() for maindir in maindirs if '500_' in maindir]
    return categories

categories = loadStims()
 
def imSelect(categories, nStim):
    for category in categories:
        trialStims = [random.sample(filePathlist, nStim) for filePathlist in category]
    return trialStims

trial1 = imSelect(categories, 14)
#clothing = Category('500_clothing').categCreate()
#furniture = Category('500_furniture').categCreate()





#props = <some list here>
#objects = [MyClass(property=foo, property2=prop) for prop in props]
#for obj in objects:
#    obj.do_stuff(variable=foobar)


#objs = [MyClass() for i in range(10)]
#for obj in objs:
#    other_object.add(obj)
#
#objs[0].do_sth()

    
    
#[f(x) for x in sequence if condition]

    #    for folder in os.listdir():
#        if '500_' in folder:
#            Category(str(folder)).categCreate()
