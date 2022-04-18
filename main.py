# Define initial variables

# Kinematics

import math

xposini = ''
xposfin = ''
ypos = ''
disp = ''
vini = ''
vfin = ''
accel = ''
timevar = ''
var_list = [xposini, xposfin, ypos, disp, vini, vfin, accel, timevar]

req_check1_list = [vfin, vini, accel, timevar]
req_check1 = 0
req_check2_list = [xposfin, xposini, vini, timevar, accel]
req_check2 = 0
req_check3_list = [vfin, vini, accel, xposfin, xposini]
req_check3 = 0
calc_fail = False
cycle_count = 0

def kin_calc(xposinit, xposfin, ypos, disp, vini, vfin, accel, timevar):
    while calc_fail == False:
        print('Calculating...')
        if req_check1 == 0:
            for x in req_check1_list:
                if type(x) == float:
                    req_check1 += 1
        if req_check1 == 3:
            if type(vini) == float and type(accel) == float and type(timevar) == float:
                vfin = vini + (accel * timevar)
            elif type(vfin) == float and type(accel) == float and type(timevar) == float:
                vini = vfin - (accel * timevar)
            elif type(vfin) == float and type(vini) == float and type(timevar) == float:
                accel = (vfin - vini) / timevar
            elif type(vfin) == float and type(vini) == float and type(accel) == float:
                timevar = (vfin - vini) / accel
            else:
                print("calculation error")
                quit()
        if req_check2 == 0:
            for x in req_check2_list:
                if type(x) == float:
                    req_check2 += 1
        if req_check2 == 4:
            if type(xposini) == float and type(vini) == float and type(timevar) == float and type(accel) == float:
                xposfin = xposini + (vini * timevar) + 0.5 * accel * (timevar ** 2)
            if type(vini) == float and type(timevar) == float and type(accel) == float and type(xposfin) == float:
                xposini = (-1 * vini) * timevar - 0.5 * accel * (timevar ** 2) + xposfin
            if type(xposini) == float and type(accel) == float and type(timevar) == float and type(xposfin) == float:
                vini = ((-1 * xposini) - 0.5 * accel * (timevar ** 2) - xposfin) * (1 / timevar)
            if type(xposini) == float and type(vini) == float and type(timevar) == float and type(xposfin) == float:
                accel = (-2 * (xposini + vini * timevar - xposfin)) / (timevar ** 2)
        if req_check3 == 0:
            for x in req_check3_list:
                if type(x) == float:
                    req_check3 += 1
        if req_check3 == 4:
            if type(vini) == float and type(accel) == float and type(xposfin) == float and type(xposini) == float:
                vfin = math.sqrt((vini ** 2) + 2 * accel * (xposfin - xposini))
            if type(accel) == float and type(xposfin) == float and type(xposini) == float and type(vfin) == float:
                vini = math.sqrt(-2 * accel * (xposfin - xposini) + (vfin ** 2))
            if type(vfin) == float and type(vini) == float and type(xposfin) == float and type(xposini) == float:
                accel = ((vfin ** 2) - (vini **2)) / (2 * (xposfin - xposini))
            if type(vfin) == float and type(vini) == float and type(accel) == float and type(xposini) == float:
                xposfin = (((vfin ** 2) - (vini ** 2)) / 2 * accel) + xposini
            if type(vfin) == float and type(vini) == float and type(accel) == float and type(xposfin) == float:
                xposini = -1 * ((((vfin ** 2) - (vini ** 2)) / 2 * accel) - xposfin)
        cycle_count += 1
        if cycle_count > 5:
            calc_fail = True
    for x in var_list:
        print(f'{x = }')
        




calc_start = input("Is this a one dimensional or two dimensional kinematics problem? type 1 or 2")
if calc_start == 1:
    print('Please input the known variables.')
    known_var = input('Do we know the initial x position?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        xposinit = input('Input the initial x value')
    known_var = input('Do we know the final x position?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        xposfin = input('Input the final x value')
    known_var = input('Do we know the initial velocity?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        vini = input('Input the initial velocity')
    known_var = input('Do we know the final velocity?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        vfin = input('Input the final velocity')
    known_var = input('Do we know the acceleration?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        accel = input('Input the acceleration')
    known_var = input('Do we know the time period?')
    known_var = known_var.upper()
    if known_var == 'Y' or 'YES':
        timevar = input('Input the time period in seconds')
    for x in var_list:
        if type(x) == int:
            x = float(x)
        elif type(x) != float:
            x == 'unknown'
elif calc_start == 2:
    print('two dimensional kinematics are not supported yet')
else:
    print('Valid input was not entered')
    quit()    
