N = int(input())

# the actual umbrellas amount to buy at each location
homeUmbrellas, workUmbrellas = 0, 0
# the umbrellas amount at each location
virtualHomeUmbrellas, virtualWorkUmbrellas = 0, 0

for i in range(N):
    goingWeather, comeWeather = [x for x in input().split()]

    if goingWeather == 'chuva' and comeWeather == 'chuva':
        if virtualHomeUmbrellas == 0:
            homeUmbrellas += 1
            virtualHomeUmbrellas += 1
    elif goingWeather == 'chuva':
        if virtualHomeUmbrellas == 0:
            homeUmbrellas += 1
            virtualWorkUmbrellas += 1
        else:
            virtualHomeUmbrellas -= 1
            virtualWorkUmbrellas += 1
    elif comeWeather == 'chuva':
        if virtualWorkUmbrellas == 0:
            workUmbrellas += 1
            virtualHomeUmbrellas += 1
        else:
            virtualWorkUmbrellas -= 1
            virtualHomeUmbrellas += 1

print(str(homeUmbrellas) + ' ' + str(workUmbrellas))
