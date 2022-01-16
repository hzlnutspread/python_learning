# if __name__ == '__main__'
# can run as a standalone program
# module can be imported and used by other modules

# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ varaible a value of '__main__' if its the initial module being run
# then python will execute the code found within __main__

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")
    # check to see if user is running this as a standalone module or importing from another module
    pass


import module_one
print(__name__)
print(module_one.__name__)
    # second print statement will print module_one as __name__ will be assigned the name of the module