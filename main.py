import time
#
# NUM_OF_ELECTRODES = 14
# NUM_OF_VALUES_FOR_EACH_ELEC = 512
#
# fileName = "EEGLogger.csv"
# file1 = open(fileName, 'r')
# data = [[] * NUM_OF_ELECTRODES]
# for i in range(NUM_OF_ELECTRODES):
#     data[i]= file1.readline()
# file1.close()

queue=[]
Electrode1=0
Electrode2=1
amountElectrodes=2
numOfQuestion=int(input("How many questions do you want to ask?"))
data=[[[] for i in range(amountElectrodes)]for j in range(numOfQuestion)]
for i in range(numOfQuestion):
    j = 0
    try:
        while True:
            time.sleep(1)
            queue.append(j)
            print(j) # 128 rows a second
            j+=1
            #if(queue.Count==(128*60)+1):# if the queue is full of a minute of inofmration
            # one extra, so that when I press than exactly 4 numbers.
            if(queue.count==5):
                 queue.pop()
    except KeyboardInterrupt:
        print("input for another 4 second")
        pass


    start_time = time.time()
    seconds = 4
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > seconds:
            print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
            break

    # according to what electrode it is we put it in a different place.

    while(len(queue)>0):
        value=queue.pop()
        data[i][Electrode1].append(value)

    print(data)
