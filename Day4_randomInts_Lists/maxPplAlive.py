import heapq

def say_hello():
    print('Hello World')

for i in range(5):
    say_hello()

"""
    # [
    # {"name": "Joe", "birth":1900, "death":1930}
    # {"name": "John", "birth":1928, "death":1925}
    

Given an array of people profiles,
1) assume the input data is valid, the death is either > birth
or None if the person is still alive.
2) birth and death could be same year, considered as "alive" that year

Find out what was the year, when most of the people were alive.
1) If it were to be a range of years, return any year within that range

Approach:
1) scan thru the people profiles, log the birth events and
death events with the timeline
2) put the events into a PriorityQueue (minHeap), sort by year
3) maintain 3 variables
    cur_people_alive
    max_people_alive
    max_alive_year
4) return the max_alive_year (integer)

N people
Time: 0(NlogN)
Space: 0(N)
"""
profiles = [{"name": "Joe", "birth":1900, "death":1930}, {"name": "John", "birth":1928, "death":1925}, {"name": "Johnny", "birth":1928, "death":1926}, {"name": "Jack", "birth":1912, "death":1945}, {"name": "Jackie", "birth":1908, "death":1919}, {"name": "Joseph", "birth":1918, "death":1949}]


def find_max_alive_year(profiles):
    """......."""
    events = list()
    cur_people_alive = 0
    max_people_alive = 0
    max_alive_year = None

    for people in profiles:
        # name = people.get('name')
        birth_year = people.get('birth')
        death_year = people.get('death')
        # -1 for sorting, process birth events first
        # if years are same
        heapq.heappush(events, (birth_year, -1))
        heapq.heappush(events, (death_year, 1))

    while events:
        year, event = heapq.heappop(events)
        cur_people_alive -= event

        while events and events[0][0] == year:
            cur_people_alive -= heapq.heappop(events)[-1]
            if cur_people_alive > max_people_alive:
                max_people_alive = cur_people_alive
                max_alive_year = year

        if cur_people_alive > max_people_alive:
            max_people_alive = cur_people_alive
            max_alive_year = year

    return max_alive_year

print(find_max_alive_year(profiles))
