import angr
proj = angr.Project("vm",auto_load_libs=False)      
simgr = proj.factory.simgr()
avoid_list=[0x400BA0,0x400B96]      
simgr.explore(find=0x400BDA,avoid=avoid_list)     
print(simgr.found[0].posix.dumps(0))
