from datetime import time, datetime
FORMAT = '%H:%M'

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
    if hour_init=='00:00':
        hour_init='01:00'
    last_hour =hour_init
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
            # print('rango 1 ')
            if hour_end >= r_start and  hour_end <= r_end1:
                # print('inside',datetime.strptime(hour_end, FORMAT) , datetime.strptime(last_hour, FORMAT))
                time = datetime.strptime(hour_end, FORMAT) - datetime.strptime(last_hour, FORMAT)
                duration = time.total_seconds()
                hours_by_range.append(divmod(duration, 3600)[0]) 
            else:
                # print('outside')
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
    case1 = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
    total = 0
    # case1 = 'RENE=MO08:00-19:00'
    if '=' in case1:
        [name,schedule]= case1.split('=')
        hours = schedule.split(',')
        hours_worked = 0
        # if len(hours)>0:
        for data in hours:
            [hour_init,hour_end] = data[2::].split('-')
            total_day= divide_in_range(data[0:2], hour_init, hour_end)
            print(data[0:2], hour_init, hour_end, total_day)
            total += total_day

        print(name,'sche', schedule)
        print(hours)
        print(total)


if __name__ == '__main__':    
    print('test')
