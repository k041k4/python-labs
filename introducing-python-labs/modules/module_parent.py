from module_child import start,init

def execute_seeding( *args, **kwargs):
    print('PARENT')
    print ('args list =', args)
    print ('keyword args dict =', kwargs)
    print('-----')


execute_seeding()
init()