import re
import sys
from common.logging import get_logger
from common.filter_params import FilterParams

# import numpy as np
# import pytz



class MarbleProcessor(FilterParams):

    def __init__(self):
        self._logger = get_logger()
        
    def process_marbles(self,collection, json_config_path):

        self._set_params(json_config_path)


        self._logger.info(f"Starting processing for marbles")

        to_be_sorted=[]
       
        for m in range(len(collection)):
            unit=collection[m]

            #filter out small marbles
            if self.size:
                if self._check_weight(unit):
                    pass
                else:
                    continue
            else:
                continue

            #filter out marbles that dont have palendrome names
            
            if self.name:
                if self._check_name(unit):
                    pass
                else:
                    continue
            else:
                continue

            to_be_sorted.append(unit)

        #sort the marbles tht were collected

        if self.color:
            sorted_marbles = self._sort_marbles_by_colors(to_be_sorted)
            self._logger.info(f"this is the sorted list of marbles: {sorted_marbles}")
            return sorted_marbles

        else:
            self._logger.info("I havent decided what should be returned if the config is empty")

    def _check_weight(self, marble):
        if marble['weight'] >= float(self.size_constraint):
           # self._logger.info(f"yes, marble of size {marble['weight']} is greater than {float(self.size_constraint)}")
            return True
        else:
            return False

    def _check_name(self, marble):

        name= marble['name']
        name= name.lower()
        name = ''.join(char for char in name if char.isalpha())
        name = name==name[::-1]
        if name:
           # self._logger.info("yes is palenrome")
            return True
        else:
           # self._logger.info("not palenrome")
            return False

    def _sort_marbles_by_colors(self, marbles):
        color_map={'R':'red','B':'blue','O':'orange','Y':'yellow','G':'green','I':'indigo','V':'violet'}
    
        color_pattern_longform_list=[]
        for i in self.color_pattern:
            color_pattern_longform_list.append(color_map[i])

        order_list_dict = {color: index for index, color in enumerate(color_pattern_longform_list)}
        marbles_sorted = sorted(marbles, key=lambda i: order_list_dict[i["color"]])

    #    self._logger.info(f" this is marbles sortd :{marbles_sorted}")
    #    self._logger.info(f" this is goal list :{color_pattern_longform_list}")

        return marbles_sorted


