from datetime import time, datetime, timedelta
import os 
import argparse

path = os.getcwd()
FORMAT = '%H:%M'
FILE =  'ioet_solution/schedule.txt'
week = ['MO','TU','WE','TH','FR']
weekend = ['SA','SU']
days_hour = {
    'week':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'weekend':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[30,20,25]},
}

def divide_in_range(day, hour_init, hour_end):
    day_range = days_hour[day]['ranges']
    price = days_hour[day]['prices']
    hours_by_range = []
    last_hour =hour_init
    total_day = 0
    flag = 0
    if hour_init.strftime(FORMAT)=='00:00':
        hour_init = hour_init+ timedelta(minutes=1)

    for rng in day_range:        
        [start,end] = rng.split('-')
        r_start = datetime.strptime(start, FORMAT)
        r_end = datetime.strptime(end, FORMAT)
        if flag ==1:
            hour_init= r_start
            flag=0

        if r_end.strftime(FORMAT) == '00:00': #
            r_end1 = r_end- timedelta(minutes=1)+ timedelta(days=1)
        else:
            r_end1 = r_end

        if hour_init >= r_start  and hour_init <= r_end1 :
            if hour_end >= r_start and  hour_end <= r_end1:
                if hour_end.strftime(FORMAT) =='00:00':
                    time1 = hour_end+ timedelta(days=1)- last_hour
                else:
                    time1 = hour_end - last_hour
                duration = time1.total_seconds()
                hours_by_range.append(round(duration/float(3600))) 
            else:
                if r_end.strftime(FORMAT) =='00:00':
                    time1 =r_end + timedelta(days=1)- last_hour
                else:
                    time1 = r_end - last_hour
                duration = time1.total_seconds()
                hours_by_range.append(round(duration/float(3600))) 
                last_hour = r_end
                flag=1
        else:
            hours_by_range.append(0) 
    total= sum([a*b for a,b in zip(hours_by_range, price)])
    return total

def main():
    parser = argparse.ArgumentParser(description='Get the hours worked from file.txt')
    parser.add_argument('--file', dest='file', default="schedule.txt",
                    help='Get the hours worked from users hours written in a file.txt (default file name: schedule.txt)')
    args = parser.parse_args()
    file_name = args.file
    data_text = []
    try:
        with  open(os.path.join(path,file_name),'r') as f:
            data_text = f.read().splitlines() 
    except Exception as error:
        print('Error:',error)
        
    for case in data_text:
        total = 0
        try:
            if '=' in case:
                [name,schedule]= case.split('=')
                hours = schedule.split(',')
                hours_worked = 0
                for data in hours:
                    [init,end] = data[2::].split('-')
                    total_day=0
                    hour_init = datetime.strptime(init, FORMAT)
                    hour_end = datetime.strptime(end, FORMAT)
                    if hour_end < hour_init and hour_end.strftime(FORMAT)!='00:00':
                        error = f'La hora de entrada debe ser mayor que la salida, verifique el formato de {name}'
                        raise Exception(error)
                    if data[0:2] in week:
                        day = 'week'
                    elif data[0:2] in weekend:
                        day = 'weekend'
                    else:
                        message = f'El código del día es erroneo, verifique el formatp de {name}'
                        raise Exception(message)
                    total_day= divide_in_range(day, hour_init, hour_end)
                    total += total_day
                message = f'The amount to pay {name} is: {total} USD'
                print(message)
                print('*******************************************************************************')
        except Exception as error:
            message = f'Msg: Data erronea verifique el formato : {case}'
            error = f'Error: {error}'
            print(message)
            print(error)
            print('*******************************************************************************')


if __name__ == '__main__':
    main()