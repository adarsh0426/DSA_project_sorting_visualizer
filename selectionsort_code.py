import time

def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1,len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if min_index!=i :
            (data[i], data[min_index]) = (data[min_index], data[i])
            drawrectangle(data, ['blue' if x == i or x == min_index else 'red' for x in range(len(data))] )
            time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])

