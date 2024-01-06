
from Collage.ImageProcessor import crop_ans
import numpy as np

def meta_calculator(img):
    br = []
    crop = img
    br.append(crop_ans.process_image_and_array(crop[20:50,20:75]))
    br.append(crop_ans.process_image_and_array(crop[45:70,20:75]))
    br.append(crop_ans.process_image_and_array(crop[65:90,20:75]))
    br.append(crop_ans.process_image_and_array(crop[85:105,20:75]))
    br.append(crop_ans.process_image_and_array(crop[100:120,20:75]))

    br.append(crop_ans.process_image_and_array(crop[120:140,20:75]))
    br.append(crop_ans.process_image_and_array(crop[140:160,20:75]))
    br.append(crop_ans.process_image_and_array(crop[160:180,20:75]))
    br.append(crop_ans.process_image_and_array(crop[175:195,20:75]))
    br.append(crop_ans.process_image_and_array(crop[190:215,20:75]))

    br.append(crop_ans.process_image_and_array(crop[210:230,20:75]))
    br.append(crop_ans.process_image_and_array(crop[225:250,20:75]))
    br.append(crop_ans.process_image_and_array(crop[245:265,20:75]))
    br.append(crop_ans.process_image_and_array(crop[260:285,20:75]))
    br.append(crop_ans.process_image_and_array(crop[280:300,20:75]))

    br.append(crop_ans.process_image_and_array(crop[295:320,20:75]))
    br.append(crop_ans.process_image_and_array(crop[315:340,20:75]))
    br.append(crop_ans.process_image_and_array(crop[335:355,20:75]))
    br.append(crop_ans.process_image_and_array(crop[350:375,20:75]))
    br.append(crop_ans.process_image_and_array(crop[370:385,20:75]))


    #Second_column_95-150

    br.append(crop_ans.process_image_and_array(crop[5:25,95:150]))
    br.append(crop_ans.process_image_and_array(crop[25:50,95:150]))
    br.append(crop_ans.process_image_and_array(crop[45:70,95:150]))
    br.append(crop_ans.process_image_and_array(crop[65:90,95:150]))
    br.append(crop_ans.process_image_and_array(crop[80:105,95:150]))

    br.append(crop_ans.process_image_and_array(crop[120:140,95:150]))
    br.append(crop_ans.process_image_and_array(crop[140:160,95:150]))
    br.append(crop_ans.process_image_and_array(crop[160:180,95:150]))
    br.append(crop_ans.process_image_and_array(crop[175:195,95:150]))
    br.append(crop_ans.process_image_and_array(crop[190:215,95:150]))

    br.append(crop_ans.process_image_and_array(crop[210:230,95:150]))
    br.append(crop_ans.process_image_and_array(crop[225:250,95:150]))
    br.append(crop_ans.process_image_and_array(crop[245:265,95:150]))
    br.append(crop_ans.process_image_and_array(crop[260:285,95:150]))
    br.append(crop_ans.process_image_and_array(crop[280:300,95:150]))

    br.append(crop_ans.process_image_and_array(crop[295:315,95:150]))
    br.append(crop_ans.process_image_and_array(crop[315:335,95:150]))
    br.append(crop_ans.process_image_and_array(crop[330:350,95:150]))
    br.append(crop_ans.process_image_and_array(crop[350:375,95:150]))
    br.append(crop_ans.process_image_and_array(crop[370:388,95:150]))


    #Third_column_175-230


    br.append(crop_ans.process_image_and_array(crop[20:50,175:230]))
    br.append(crop_ans.process_image_and_array(crop[45:70,175:230]))
    br.append(crop_ans.process_image_and_array(crop[65:90,175:230]))
    br.append(crop_ans.process_image_and_array(crop[85:110,175:230]))
    br.append(crop_ans.process_image_and_array(crop[100:120,175:230]))

    br.append(crop_ans.process_image_and_array(crop[120:140,175:230]))
    br.append(crop_ans.process_image_and_array(crop[140:160,175:230]))
    br.append(crop_ans.process_image_and_array(crop[160:180,175:230]))
    br.append(crop_ans.process_image_and_array(crop[175:195,175:230]))
    br.append(crop_ans.process_image_and_array(crop[190:215,175:230]))

    br.append(crop_ans.process_image_and_array(crop[210:230,175:230]))
    br.append(crop_ans.process_image_and_array(crop[225:250,175:230]))
    br.append(crop_ans.process_image_and_array(crop[245:265,175:230]))
    br.append(crop_ans.process_image_and_array(crop[260:285,175:230]))
    br.append(crop_ans.process_image_and_array(crop[280:300,175:230]))

    br.append(crop_ans.process_image_and_array(crop[295:320,175:230]))
    br.append(crop_ans.process_image_and_array(crop[315:335,175:230]))
    br.append(crop_ans.process_image_and_array(crop[335:355,175:230]))
    br.append(crop_ans.process_image_and_array(crop[350:370,175:230]))
    br.append(crop_ans.process_image_and_array(crop[370:388,175:230]))

    #fourth_column_250-305

    br.append(crop_ans.process_image_and_array(crop[5:25,250:305]))
    br.append(crop_ans.process_image_and_array(crop[25:50,250:305]))
    br.append(crop_ans.process_image_and_array(crop[45:70,250:305]))
    br.append(crop_ans.process_image_and_array(crop[65:90,250:305]))
    br.append(crop_ans.process_image_and_array(crop[80:105,250:305]))


    br.append(crop_ans.process_image_and_array(crop[105:120,250:305]))
    br.append(crop_ans.process_image_and_array(crop[120:140,250:305]))
    br.append(crop_ans.process_image_and_array(crop[140:160,250:305]))
    br.append(crop_ans.process_image_and_array(crop[155:175,250:305]))
    br.append(crop_ans.process_image_and_array(crop[175:195,250:305]))

    #cv2.imshow("img",crop[175:205,250:305])
    #cv2.waitKey(0)
    br.append(crop_ans.process_image_and_array(crop[210:230,250:305]))
    br.append(crop_ans.process_image_and_array(crop[225:250,250:305]))
    br.append(crop_ans.process_image_and_array(crop[245:265,250:305]))
    br.append(crop_ans.process_image_and_array(crop[260:275,250:305]))
    br.append(crop_ans.process_image_and_array(crop[280:300,250:305]))

    br.append(crop_ans.process_image_and_array(crop[295:320,250:305]))
    br.append(crop_ans.process_image_and_array(crop[315:335,250:305]))
    br.append(crop_ans.process_image_and_array(crop[335:355,250:305]))
    br.append(crop_ans.process_image_and_array(crop[350:370,250:305]))
    br.append(crop_ans.process_image_and_array(crop[370:388,250:305]))

    #fifth_column_325-385


    br.append(crop_ans.process_image_and_array(crop[5:25,325:385]))
    br.append(crop_ans.process_image_and_array(crop[25:50,325:385]))
    br.append(crop_ans.process_image_and_array(crop[45:70,325:385]))
    br.append(crop_ans.process_image_and_array(crop[65:85,325:385]))
    br.append(crop_ans.process_image_and_array(crop[80:105,325:385]))

    br.append(crop_ans.process_image_and_array(crop[120:140,325:385]))
    br.append(crop_ans.process_image_and_array(crop[140:160,325:385]))
    br.append(crop_ans.process_image_and_array(crop[160:180,325:385]))
    br.append(crop_ans.process_image_and_array(crop[175:195,325:385]))
    br.append(crop_ans.process_image_and_array(crop[190:215,325:385]))

    br.append(crop_ans.process_image_and_array(crop[210:230,325:385]))
    br.append(crop_ans.process_image_and_array(crop[225:250,325:385]))
    br.append(crop_ans.process_image_and_array(crop[245:265,325:385]))
    br.append(crop_ans.process_image_and_array(crop[260:285,325:385]))
    br.append(crop_ans.process_image_and_array(crop[280:300,325:385]))

    br.append(crop_ans.process_image_and_array(crop[295:320,325:385]))
    br.append(crop_ans.process_image_and_array(crop[315:335,325:385]))
    br.append(crop_ans.process_image_and_array(crop[335:355,325:385]))
    br.append(crop_ans.process_image_and_array(crop[350:370,325:385]))
    br.append(crop_ans.process_image_and_array(crop[370:388,325:385]))

    
    return np.array(br)
    print(br)

def calculate_imgage(ans_sheet,exam_sheet):
    
    ans_result = meta_calculator(ans_sheet)
    exam_result = meta_calculator(exam_sheet)
    
    
    physics =  np.sum(exam_result[:25] ==  ans_result[:25] )
    chemistry =  np.sum(exam_result[25:40] ==  ans_result[25:40] )
    math =  np.sum(exam_result[40:70] ==  ans_result[40:70] )
    english =  np.sum(exam_result[70:85] ==  ans_result[70:85] )
    analytical =  np.sum(exam_result[85:100] ==  ans_result[85:100] )

    
    
    
    # print(int(physics))
    
    return {
        "physics":int(physics),
        "chemistry":int(chemistry),
        "math":int(math),
        "english":int(english),
        "analytical":int(analytical),
    }

