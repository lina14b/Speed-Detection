import time
import cv2
import os
class Vehicle:
    def __init__(self, class_type, vehicle_id,FirstCentre_y):
        self.FirstCentre_y=FirstCentre_y
        self.class_type = class_type
        self.vehicle_id = vehicle_id
        self.top_box = None
        self.top_frame = None
        self.bottom_box = None
        self.bottom_frame = None
        self.vitesse = None
        self.image = None
    def print(self):
        print(self.class_type,"-",self.vehicle_id)
        print("\n")
    
    def Top_Crossed(self,box,framenb):
        self.top_box=box
        self.top_frame=framenb#time.time()
        #self.vitesse= framenb#str(self.top_time)
    
    def Bottom_Crossed(self,box,framenb):
        self.bottom_box=box
        self.bottom_frame=framenb #time.time()
       # self.vitesse= framenb#str(self.bottom_time)


    def calcul_vitesse(self,fps,distance):
        annotation=""
        if self.top_frame is not None and self.bottom_frame is not None:
            frames_between_points=abs(self.top_frame-self.bottom_frame)
            time_actual = frames_between_points / fps
            self.vitesse= str(int((distance/time_actual)*3.6 ))+" Km/h"#time_actual
            annotation=self.vitesse
        return annotation

    def crop_and_save(self,image):
        x1, y1, x2, y2 = self.bottom_box
        cropped_image = image[y1:y2, x1:x2]
        output_path = os.path.join("images", str(self.vehicle_id)+".jpg")
        cv2.imwrite(output_path, cropped_image)
        print(output_path)

      
            