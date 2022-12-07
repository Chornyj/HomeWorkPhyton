import random
'''
data = [random.randint(1,100) for _ in range(1000)]
print(data)'''

#Algoritm sorting

def my_sort1(data):
    for element_number1 in range(0,len(data)):
       # print(f'Nomer elementu jakyj perevirajemo ',element_number1)
        for element_number2 in range(element_number1,len(data)):
            #print('Номер елементу з яким ми перевіряємо',element_number2)
            if data[element_number2] < data[element_number1]: #zamina misciamy elementiv
                data[element_number1],data[element_number2] = data[element_number2],data[element_number1]
    return data

'''
        

data = [random.randint(1,1000) for _ in range(10000)]
#print(
my_sort1(data))

data.my_sort1(1000)
'''
def mysort2(data):
    if len(data)<=1:
        return data
    center_element = data[0]
    left,middle,right = [],[],[]
    for element in data:
        if element<center_element:
            left.append(element)
        if element==center_element:
            middle.append(element)
        #if element>center_element:
          #  right.append(element)

    return mysort2(left) + middle + mysort2(right)
        
data= [random.randint(1,1000) for _ in range(10000)]

start = datatime.now()
my_sort1(data)
end = datatime.now()

start = datatime.now()
mysort2(data)
end = datatime.now()

    
