import random

results={}
for i in range(1000):
    num_1=random.randint(1,6)
    num_2=random.randint(1,6)
    sum=num_1+num_2
    if sum in results:
        results[sum]+=1
    else:
        results[sum]=1
for key, value in results.items():
    vids=(value / 1000) * 100
    vids_2= (1/36) * 100
    print(f'Сума шестигранних кісток: {round(key)} ; в діапазоні 1000 випала {round(value)} разів; '
          f'відсоток симуляції: {round(vids)}; очікуваний відсоток: {round(vids_2)}')

