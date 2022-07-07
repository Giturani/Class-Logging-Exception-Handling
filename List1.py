import logging
import log_file

class List1 :
    def __init__(self , l1):
        self.l2 = l1

    def reverse1(self):
        """reverse the list"""
        try:
            logging.info("try to reverse the list")
            if type(self.l2) == list:
                return self.l2[::-1]
            else:
                logging.info("Data is not a list.Not possible to reverse now")
        except Exception as e:
            logging.exception(e)

    def access_num(self) :
        """Accessing the particular Number"""
        try:
            logging.info("Accessing Particular number")
            b = int(input("Please enter a number which you have to access "))
            values = []
            for i in self.l2:
                if i == b:
                    values.append(i)
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if j == b:
                            values.append(j)
                if type(i) == dict:
                    for j, k in i.items():
                        if j == b:
                            values.append(j)
                        if k == b:
                            values.append(k)
            if len(values) == 0:
                logging.info("We dont find entered number in the list %d",b)
            else:
                return values
        except Exception as e:
            logging.exception(e)

    def access_string(self) :
        """Accessing particular string"""
        try:
            logging.info("Accessing particular string")
            s = input("Please enter a string which you have to access ")
            values = []
            for i in self.l2:
                if i == s:
                    values.append(i)
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if j == s:
                            print(j)
                            values.append(j)
                if type(i) == dict:
                    for j, k in i.items():
                        if j == s:
                            values.append(j)
                        if k == s:
                            values.append(k)
            if len(values) == 0:
                logging.info("We dont find the entered string in the collection %s",s)
            else:
                return values
        except Exception as e:
            logging.exception(e)

    def extract_list(self) :
        """Extract List entity from collection"""
        try:
            logging.info("Extract List Entity from collection")
            lists = []
            for i in self.l2:
                if type(i) == list:
                    lists.append(i)
            if len(lists) == 0:
                logging.info("we dont have any list entity in the collection")
            else:
                return lists
        except Exception as e:
            logging.exception(e)

    def extract_dict_keys(self):
        """Accessing dictionary Keys from the list"""
        try:
            logging.info("Extracting Keys from the collection")
            dict_keys = []
            for i in self.l2:
                if type(i) == dict:
                    dict_keys.append(i.keys())
            return dict_keys
        except Exception as e:
            logging.exception(e)

    def extract_dict_values(self):
        """Accessing dictionary values from the list"""
        try:
            logging.info("Extracting dictionary values from the collection")
            dict_values = []
            for i in self.l2:
                if type(i) == dict:
                   dict_values.append(i.values())
            return dict_values
        except Exception as e:
            logging.exception(e)


l1 = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" : "sudh" , 234 : [23,45,656]}]
#l1 = (3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" : "sudh" , 234 : [23,45,656]})
obj = List1(l1)
logging.info(obj.reverse1())
logging.info(obj.access_num())
logging.info(obj.access_string())
logging.info(obj.extract_list())
logging.info(obj.extract_dict_keys())
logging.info(obj.extract_dict_values())
