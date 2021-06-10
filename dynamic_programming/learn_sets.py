val = '/XCPU_0/CPU_0/CORE_0   0.0 100.0    0.0    0.0    0.0      0.0  9449 '
check_strings = ['%exec', '%srun']

if set(check_strings) and set(val.split(' ')):
    print("Found")
else:
    print("Not found")
    
if set(check_strings) & set(val.split(' ')):
    print("Found")
else:
    print("Not found")
    