Inputs = int(input());
Observations = []

for i in range (Inputs):
    Observation = {};
    Line = input().split()
    Observation['time'] = int(Line[0])
    Observation['pos'] = int(Line[1])
    Observations.append(Observation)

def get_time(dict):
    return dict['time']

# Hash table sort, ["15": 2], ["2": 3] -> ["2": 3], ["15": 2]
Observations.sort(key = get_time)

fastestSpeed = 0;

for x in range (len(Observations) - 1):
  Time = Observations[x+1]['time'] - Observations[x]['time']
  Pos = abs(Observations[x+1]['pos'] - Observations[x]['pos'])

  if (Pos / Time > fastestSpeed):
    fastestSpeed = Pos / Time

print (fastestSpeed)
