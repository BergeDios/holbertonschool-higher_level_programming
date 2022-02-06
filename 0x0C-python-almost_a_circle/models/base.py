#!/usr/bin/python3
"""Module base"""
import json
import csv


class Base:
    """ base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization method"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ pass list to json representation"""

        if list_dictionaries == None or list_dictionaries == "[]":
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object to file"""

        filename = f"{cls.__name__}.json"
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ json string to dict"""

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""

        if cls.__name__ == "Rectangle":
            new = cls(10,10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new
    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""

        filename = f"{cls.__name__}.json"
        list_ins = []

        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                list_ins.append(cls.create(**instances[i]))
        except:
            pass
        return list_ins
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize to csv"""

        filename = cls.__name__ + ".csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs
