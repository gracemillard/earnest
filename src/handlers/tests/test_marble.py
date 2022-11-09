from processor.marble_processor import MarbleProcessor
#from common.filter_params import FilterParams
import pandas as pd
import json


'''
This is actually the same as the handler, 
I include this file in two places out of habit, but I dont need them both for this assignment
'''

def main(collection):

    if not collection:
        raise ValueError("Empty collection, cannot proceed")



    json_config_path="resources/filters.json"
    marble_processor = MarbleProcessor()
    marble_processor.process_marbles(collection,json_config_path)


''''
I was considering another approach here
'''
    #for i in range(len(collection)):
    #    unit=collection[i]
    #    marble_processor.process_marbles(unit)


if __name__ == "__main__":
    print("running")
    collection= [
        {"id": 1, "color": "blue", "name": "Bob", "weight": 0.5 },
        { "id": 2, "color": "red", "name": "John Smith", "weight": 0.25 },
        { "id": 3, "color": "violet", "name": "Bob O'Bob", "weight": 0.5 },
        { "id": 4, "color": "indigo", "name": "Bob Dad-Bob", "weight": 0.75 },
        { "id": 5, "color": "yellow", "name": "John", "weight": 0.5 },
        { "id": 6, "color": "orange", "name": "Bob", "weight": 0.25 },
        { "id": 7, "color": "blue", "name": "Smith", "weight": 0.5 },
        { "id": 8, "color": "blue", "name": "Bob", "weight": 0.25 },
        { "id": 9, "color": "green", "name": "Bobb Ob", "weight": 0.75 },
        { "id": 10, "color": "blue", "name": "Bob", "weight": 0.5 }
        ]
    main(collection)
    print("processinng complete")
