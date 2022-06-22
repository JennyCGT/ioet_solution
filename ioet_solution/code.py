from datetime import time, datetime, timedelta
import os 
path = os.getcwd()
FORMAT = '%H:%M'
FILE =  'ioet_solution/schedule.txt'
print(os.path.join(path,FILE))
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
    if hour_init=='00:00':
        hour_init='00:01'
    elif hour_init=='09:00':
        hour_init='09:01'
    elif hour_init=='18:00':
        hour_init='18:01'
    total_day = 0
    flag = 0
    for rng in day_range:        
        [r_start,r_end] = rng.split('-')
        if flag ==1:
            hour_init= r_start
        if r_end == '00:00':
            r_end1 = '23:59'
        else:
            r_end1 = r_end
        # print('range',r_start, r_end, 'sche', hour_init, hour_end)
        # print(hour_init >= r_start  , hour_init <= r_end1 )
        if hour_init >= r_start  and hour_init <= r_end1 :
            # print('rango 1 ',hour_init  ,  hour_end)
            if hour_end >= r_start and  hour_end <= r_end1:
                # print('inside',datetime.strptime(hour_end, FORMAT),datetime.strptime(last_hour, FORMAT))
                if hour_end =='00:00':
                    time = datetime.strptime(hour_end, FORMAT)+ timedelta(days=1)- datetime.strptime(last_hour, FORMAT)
                else:
                    time = datetime.strptime(hour_end, FORMAT) - datetime.strptime(last_hour, FORMAT)
                duration = time.total_seconds()
                hours_by_range.append(divmod(duration, 3600)[0]) 
            else:
                # print('outside')
                if r_end =='00:00':
                    time = datetime.strptime(r_end, FORMAT)+ timedelta(days=1)- datetime.strptime(last_hour, FORMAT)
                else:
                    time = datetime.strptime(r_end, FORMAT) - datetime.strptime(last_hour, FORMAT)
                duration = time.total_seconds()
                hours_by_range.append(divmod(duration, 3600)[0]) 
                last_hour = r_end
                flag=1
        else:
            hours_by_range.append(0) 
        # print(hours_by_range,)
    # print([a*b for a,b in zip(hours_by_range, price)], price,day)
    total= sum([a*b for a,b in zip(hours_by_range, price)])
    return total
    # print(hours_by_range,'total', total)

def main():
    # case1 = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    with  open(os.path.join(path,FILE),'r') as f:
        data_text = f.read().splitlines() 
    # print(data_text)
    # print(type(data_text))
    for case in data_text:
        # case = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        total = 0
        # case1 = 'RENE=MO08:00-19:00'
        try:
            if '=' in case:
                [name,schedule]= case.split('=')
                hours = schedule.split(',')
                hours_worked = 0
                # if len(hours)>0:
                for data in hours:
                    [hour_init,hour_end] = data[2::].split('-')
                    total_day=0
                    total_day= divide_in_range(data[0:2], hour_init, hour_end)
                    total += total_day
                    # print(data[0:2], hour_init, hour_end, total_day,total)
                message = f'The amount to pay {name} is: {total} USD'
                # print('Hello')
                # print(total)
                print(message)
        except Exception as error:
            message = f'Data erronea verifique el formato : {case}'
            print(message)
            print(error)
if __name__ == '__main__':    
    print('test')
