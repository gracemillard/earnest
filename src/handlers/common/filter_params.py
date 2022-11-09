import json


{
    "filter_type":[
       "remove_pdays",
       "name_split",
       "age",
       "boolean_replacement",
       "time_reformating",
       "rename_y",
       "catogorize_address"
    ],
    "pdays_constraint":"-1",
    "age_increment":"10",
    "date_format":"dd/MM",
    "new_name":"outcome",
    "address_catagories":{"water":["lake","creek"],"relief":["hill","canyon"],"flat":["plain"]}
 }


class FilterParams():

    def __init__(self):
        self.pdays = None
        self.name = None
        self.age = None
        self.boolean_replacement = None
        self.time_reformating = None
        self.catogorize_address = None
        self.rename_y= None

        self.new_y=None
        self.pdays_constraint = None
        self.age_increment = None
        self.date_format = None
        self.new_name = None
        self.address_catagories = None



    def _read_json_config(self, json_config_path):
        with open(json_config_path) as f:
            configurations = json.load(f)
            if not configurations['filter_type']:
                raise ValueError(f"no ilters selected config might not be configred right")
            else:
                return  configurations

    def _is_pdays(self,configurations):
        
        if "pdays" in configurations['filter_type']:
            print("pdays was selected in config")
            self.pdays=True

            if configurations['pdays_constraint']:
                self.pdays_constraint=configurations['pdays_constraint']
            else:
                self.pdays_constraint= -1
                

    def _is_age(self, configurations):
        if "age" in configurations['filter_type']:
            print("age was selected in config")
            self.age=True
            if configurations['age_increment']:
                self.age_increment=configurations['age_increment']
            else:
                self.age_increment=10
    def _is_name_y(self, configurations):
        if "rename_y" in configurations['filter_type']:
            print("rename_y was selected in config")
            self.rename_y=True
            if configurations['new_name']:
                self.new_y=configurations['new_name']
            else:
                self.new_y= "outcome"

    def _is_name(self, configurations):
        if "name_split" in configurations['filter_type']:
            print("name was selected in config")
            self.name=True
            

    def _is_bool_replacement(self, configurations):
        if "boolean_replacement" in configurations['filter_type']:
            print("boolean_replacement was selected in config")
            self.boolean_replacement=True

    def _is_time_reformating(self, configurations):
        if "time_reformating" in configurations['filter_type']:
            print("time_reformating was selected in config")
            if configurations['date_format']:
                self.date_format=configurations['date_format']
            else:
                self.date_format="dd/MM"

    def _is_address(self, configurations):
        if "catogorize_address" in configurations['filter_type']:
            print("catogorize_address was selected in config")
            if configurations['address_catagories']:
                self.address_catagories=configurations['address_catagories']
            else:
                self.address_catagories={"water":["lake","creek"],"relief":["hill","canyon"],"flat":["plain"]}


    def _set_params(self,json_config_path):
        configurations = self._read_json_config(json_config_path)

        self._is_pdays(configurations)
        
        self._is_name(configurations)

        self._is_size(configurations)

    #    print(f"everthing set , here is a look {self.color_pattern}")



