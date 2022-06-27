EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
with open(EC_IO_FILE,'r+b') as file:
    flip_board=1
    file.seek(0x68)
    cpu_cur_temp = (int(file.read(1).hex(),16))
    file.seek(0x80)
    gpu_cur_temp = (int(file.read(1).hex(),16))
    file.seek(0xcc) 
    cpu_fan = (int(file.read(2).hex(),16))
    if cpu_fan != 0:
        cpu_fan = 478000//cpu_fan
    file.seek(0xca)
    gpu_fan = (int(file.read(2).hex(),16))
    if gpu_fan != 0:
        gpu_fan = 478000//gpu_fan

    print("CPU temperature : " + str(cpu_cur_temp) + "             CPU Fan Speed " + str(cpu_fan))
    print("GPU temperature : " + str(gpu_cur_temp) + "             GPU Fan Speed " + str(gpu_fan))