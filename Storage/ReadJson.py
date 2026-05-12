import json
from pathlib import Path




class Query:
    def __init__(self):
        self.path=Path(__file__).resolve().parent / 'WorkingData'/'MonitoringData.json'
        if not self.path.exists():
            raise FileNotFoundError('No Data was found. The json file that stores the monitoring data was not found')
        with open(self.path, "r") as f:
            self.json_data = json.load(f)
        

    def Get_rencent_data(self):
        # this retuns the path of the rencet 2 rasters.
        # output is of the form {0:oldest}
        output={} 
        most_recent_id=len(self.json_data)
        for dicts in self.json_data:
            if dicts['id']==most_recent_id-1:
                output[0]=dicts
            elif dicts['id']==most_recent_id-2:
                output[1]=dicts

        if len(output)==1:
            print('Only a single data exit')
            return output
        return output



    def Get_data_byid(self,id):
        data=None
        for dicts in self.json_data:
            if dicts['id']==id:
                data=dicts
                break
        
        if data==None:
            print('Data Not Found')
            return data
        
        return data
    
    def Get_by_name(self,Filename):
        data=None
        for dicts in self.json_data:
            if dicts['FileName']==Filename:
                data=dicts
                break
        
        if data==None:
            print('Data Not Found')
            return data
        
        return data
    

    def Get_data_bydate(self,date):
        #Date must be of the format 2026-05-08. this will not work for applications where multiples data are stored in a single day
        data=None
        for dicts in self.json_data:
            if dicts['DateSaved'].split()[0]==date:
                # data is stored as 2026-05-08 17-26-14.697118 in dataase
                data=dicts
                break
        
        if data==None:
            print('Data Not Found')
            return data
        
        return data
        









