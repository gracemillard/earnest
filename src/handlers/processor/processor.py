import re
import sys
from common.logging import get_logger
from common.filter_params import FilterParams
import random


class FileProcessor(FilterParams):

    def __init__(self):
        self._logger = get_logger()
        
    def process_files(self,file, json_config_path):

        self._set_params(json_config_path)
        self._logger.info(f"Starting processing for marbles")

        if self.age:
            file = self._apply_age(file)
            self._logger.info(f"applied age filter") 

        if self.name:
            file = self._apply_name(file)
            self._logger.info(f"applied name filter")          

        if self.pdays:
            file = self._apply_pdays(file)
            self._logger.info(f"applied pdays filter")
        
        if self.boolean_replacement:
            file = self._apply_bool(file)
            self._logger.info(f"applied boolean replacement")    
   
        if self.time_reformating:
            file = self._apply_time(file)
            self._logger.info(f"applied time format")
         
        if self.rename_y:
            file = self._apply_y_name(file)
            self._logger.info(f"applied y name")
        
         if self.catogorize_address:
            file, aggregated = self._apply_address(file)
            self._logger.info(f"applied address catagorization")


        self._persist_files_locally(file, aggregated)

        return file
       
    def _apply_age(self, file):
        age_increment=int(self.age_increment)
        for i in range(len(file)):
            file.loc[i,'age']=int(int(file['age'][i])/age_increment)
        return file
        
    def _apply_name(self, file):
        file[['first_name','last_name']] = file['name'].loc[file['name'].str.split().str.len() == 2].str.split(expand=True)
        return file

    def _apply_pdays(self, file):
        num=int(f"{self.pdays_constraint}")
        file.loc[file['pdays']!=num]
        return file

     def _apply_bool(self, file):
         for col in file.columns:
            if len(list(file[f'{col}'].unique())) == 2:
                if ['no','yes'] == list(file[f'{col}'].unique()):
                    print(col)
                    for i in range(len(file[f'{col}'])):
                        if file[f'{col}'][i]=='yes':
                            file.loc[i,f'{col}']=1
                        else:
                            file.loc[i,f'{col}']=0
        return file
        
    def _apply_address(self, file):
        ad=self.address_catagories
        file['catagory']=None
        for i in range(len(file)):
            entry=file["address"][i]
            entry=re.sub("(?<=[A-z])(0)(?=)", "o", entry)
            entry_2=re.sub("(?<=[A-z])(3)(?=)", "e", entry)
            entry_4=entry_2.replace("\\n", " ") #dosnt cover all cases... but its also not nessesary
            
            for j in ad:
                check_list=ad[j]
                for k in check_list:
                    if bool(re.search(f"(?<=)({k})(?=)", entry_4.lower())):
                        if file.loc[i,'catagory'] is None:
                            file.loc[i,'catagory'] = j
                        elif file.loc[i,'catagory'] == j:
                            continue
                            
                        else:
                            file.loc[i,'catagory'] = "multi_catagory_address"

        aggregated = _aggregate_by_category(file)
        return file, aggregated

    def _apply_time(self, file):
        for i in range(len(file)):
            month_i=file['month'][i]
            day_i=file['day'][i]
            month_number = datetime.datetime.strptime(f'{month_i}', '%b').month
            day_number = datetime.datetime.strptime(f'{day_i}', '%d').day
            file.loc[i,'date']=f"{month_number}/{day_number}"
        return file

        
    def _apply_y_name(self, file): 
            file.rename({'y':str(self.new_y)}, axis=1, inplace=True)
        return file

    def _aggregate_by_category(self):
        grouped=file.groupby(['catagory','age'])['catagory'].count()
        aggregated= pd.DataFrame(grouped)

        return aggregated

    def _persist_files_locally(self,file,aggregated):

        file.to_csv(f'tests/data/test_a_{random.randrange(0,100,1)}.csv')
        file.to_parquet(f'tests/data/test_a_{random.randrange(0,100,1)}.gzip', compression='gzip')



