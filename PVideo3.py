# import imageio
#imageio.plugins.ffmpeg.download()

from moviepy.editor import *
import glob
# import ffmpeg
import os




import numpy as np

films =[]


list_merge2=[]


# list_merge2=[]
# base='/media/vision/ADATA HD710M PRO/External/backup_data_reid/Uni/Reid-16-1-2023/door1/baradaran/IN/'
# for film in films:
# 	list_merge2.append(VideoFileClip(base+film))
# final2 = concatenate_videoclips(list_merge2)
# final2.write_videofile("/media/vision/ShareStorage/Data/fullvideo_merge_reid/Uni/Reid-16-1-2023/Elmosanat_2023-1-16_door1_camera2_total.mp4" ,
# codec="libx265",audio=False)		
		
films2=["D32_S20230116065930_E20230116082949.mp4","D32_S20230116082950_E20230116095654.mp4","D32_S20230116095654_E20230116111307.mp4",
             "D32_S20230116111307_E20230116111403.mp4","D32_S20230116111403_E20230116111421.mp4","D32_S20230116111421_E20230116112707.mp4",
             "D32_S20230116112707_E20230116112732.mp4","D32_S20230116112732_E20230116125039.mp4","D32_S20230116125039_E20230116135017.mp4",
             "D32_S20230116135017_E20230116135033.mp4","D32_S20230116135033_E20230116135409.mp4","D32_S20230116135409_E20230116135413.mp4",
             "D32_S20230116135413_E20230116151443.mp4","D32_S20230116151443_E20230116160057.mp4","D32_S20230116160058_E20230116160138.mp4"]
base='/media/vision/ADATA HD710M PRO/External/backup_data_reid/Uni/Reid-16-1-2023/olom_paye/'
for film in films2:
	# list_merge2.append(VideoFileClip(base+film))
    list_merge2.append(VideoFileClip(base + film))
final2 = concatenate_videoclips(list_merge2)
final2.write_videofile("/home/vision/AA/full_videos/Elmosanat_2023-1-16_doorolom_paye_camera32_total.mp4" ,codec="libx265",audio=False)






# /media/vision/ADATA HD710M PRO/External/backup_data_reid/Uni/Reid-16-1-2023/door1/baradaran/IN/D2_S20230116070122_E20230116072535.mp4
