import csv

class Firewall:
    ''' Simple firewall class
    file_path = Location of the csv rule file
    rule_dict = Accumulated jsonized rule dictionary'''

    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        self.rule_dict = {}

    def insert_rule(self, direction, proto, port ,ip):
        ''' Populates the rule dictionary which is consulted 
        for checking if a rule is hit or not'''

        root = self.rule_dict
        if direction in root.keys():
            root = root[direction]
        else:
            root[direction] = {}
            root = root[direction]
        if proto in root.keys():
            root = root[proto]
        else:
            root[proto] = {}
            root = root[proto]
        if port in root.keys():
            root = root[port]
        else:
            root[port] = []
            root = root[port]
        if ip not in root:
            root.append(ip)

    def construct_knowledge_base(self):
        ''' Converts the rule line into the rule dictionary'''

        with open(self.file_path) as csv_file:
            rules = csv.reader(csv_file, delimiter = ',')
            #count = 0
            for rule in rules:
                self.insert_rule(rule[0], rule[1], rule[2], rule[3])
                #count += 1
                #print(count)

    def interval_checker(self, observed, given_list, port):
        ''' For handling the range case mentioned in rules
            for port and ip addresses'''

        for given_data in given_list:
            if '-' in given_data:
                start = given_data.split('-')[0]
                end = given_data.split('-')[1]
                if port == True:
                    start = int(start)
                    end = int(end)
                if observed >= start and observed <= end:
                    if port == True:
                        return given_data
                    return True
        return None

    def accept_packet(self, direction, proto, port, ip):
        ''' Function that navigates the rule dictionary to check
            if a rule is hit for the packet'''

        root = self.rule_dict
        if direction not in root.keys():
            return False

        root = root[direction]
        if proto not in root.keys():
            return False

        root = root[proto]
        if str(port) in root.keys():
            root = root[str(port)]
        else:
            port_key = self.interval_checker(port, root.keys(), True)
            if port_key is None:
                return False
            root = root[port_key]

        if ip in root:
            return True
        else:
            return self.interval_checker(ip, root, False)
