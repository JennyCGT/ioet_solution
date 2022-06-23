from datetime import time, datetime, timedelta
import os 
import argparse

path = os.getcwd()
FORMAT = '%H:%M'
FILE =  'ioet_solution/schedule.txt'
days_hour = {
    'MO':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'TU':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'WE':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'TH':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'FR':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[25,15,20]},
    'SA':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[30,20,25]},
    'SU':{'ranges':['00:01-09:00','09:01-18:00','18:01-00:00'],'prices':[30,20,25]},
}

def divide_in_range(day, hour_init, hour_end):
    day_range = days_hour[day]['ranges']
    price = days_hour[day]['prices']
    hours_by_range = []
    last_hour =hour_init
    total_day = 0
    flag = 0
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
                hours_by_range.append(divmod(duration, 3600)[0]) 
            else:
                if r_end.strftime(FORMAT) =='00:00':
                    time1 =r_end + timedelta(days=1)- last_hour
                else:
                    time1 = r_end - last_hour
                duration = time1.total_seconds()
                hours_by_range.append(divmod(duration, 3600)[0]) 
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
    with  open(os.path.join(path,file_name),'r') as f:
        data_text = f.read().splitlines() 
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

                    total_day= divide_in_range(data[0:2], hour_init, hour_end)
                    total += total_day
                message = f'The amount to pay {name} is: {total} USD'
                print(message)
                print('*******************************************************************************')
        except Exception as error:
            message = f'Data erronea verifique el formato : {case}'
            print(message)
            print(error)
