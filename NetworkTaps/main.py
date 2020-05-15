master_route_arr = []

route_arr = []
route_dict = {}
tap_arr= []

def readFile():     #reads text from file to store as array
    f = open('routes.txt','r')
    for x in f:
        route_arr.append(x.rstrip().split(','))

def find_unique():
    for route in route_arr:
        for node in route:
            if(node in route_dict.keys()):
                route_dict[node] += 1   #add to dict to count how many times it occured
            else:
                route_dict[node] = 1    #add to dict to count new occurance 

def del_useless_routes():
    remove_count = 0
    most_node = max(route_dict,key = lambda key:route_dict[key])
    print('Routes to remove: ',route_dict[most_node])
    print('Most node links :',most_node)
    tmp_arr = route_arr[:]
    for route in route_arr:
        for node in route:
            if(node == most_node):
                remove_count += 1
                tmp_arr.remove(route)
    print('Total routes removed: ',len(tmp_arr))
    tap_arr.append(most_node)
    route_dict.clear()
    return tmp_arr

def refine_tap():
    refined_routes = []
    reoccur_node_arr = []
    for route in master_route_arr:
        reoccur = 0
        for node in tap_arr:
            if(route.count(node) == 1):
                reoccur += 1
        if(reoccur > 1 ):
            print(reoccur)
            print('Reoccured route: ',route)
            reoccur_node_arr.append(route)
            print(len(reoccur_node_arr))


if __name__ == '__main__':
    readFile()
    while(len(route_arr) >0):
        find_unique()
        route_arr = del_useless_routes()
    print(len(route_arr))
    print('Tap Count: ',len(tap_arr))
    print('Tap array: ',tap_arr)