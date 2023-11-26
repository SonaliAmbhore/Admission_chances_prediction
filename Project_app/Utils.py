import json
import config
import pickle
import numpy as np

class AdmissionChances():
    
    def __init__(self,GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA ,Research):
        
        self.GRE_Score = GRE_Score
        self.TOEFL_Score = TOEFL_Score
        self.University_Rating = University_Rating
        self.SOP = SOP
        self.LOR = LOR
        self.CGPA= CGPA
        self.Research = Research
        
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
    
        with open(config.JSON_FILE_PATH,'r')as f:
            self.data = json.load(f)
            
    def get_predict_chances(self):
        
        self.load_model()
        
        test_array = np.zeros(len(self.data["columns"])) 
        test_array[0] = self.GRE_Score
        test_array[1] = self.TOEFL_Score
        test_array[2] = self.University_Rating
        test_array[3] = self.SOP
        test_array[4] = self.LOR
        test_array[5] = self.CGPA
        test_array[6] = self.Research
        
        
        print("Test Array :",test_array)
        
        predict_chances = self.load_model.predict([test_array])
        
        return predict_chances
    
    
          #Adm_chs = AdmissionChances(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
          #Adm_chs.get_predict_chances()                    
            
                      
        
        
        