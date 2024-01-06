
from Collage.ImageProcessor import crop_ans
import numpy as np
import cv2
from Collage.ImageProcessor.crop_sheet import crop_sheet

def meta_calculator(img):
    br = []
    cnta = []
    crop = img
    br.append(crop_ans.process_image_and_array_for_test(crop[20:40,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[45:60,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[65:80,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[85:100,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[105:120,20:75],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[120:136,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[137:154,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[155:172,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[173:192,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[193:210,20:75],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[210:230,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[225:250,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[245:265,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[260:285,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[280:300,20:75],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[300:316,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[317:335,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[336:352,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[353:370,20:75],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[371:387,20:75],cnta))

    #Second_column_95-150

    br.append(crop_ans.process_image_and_array_for_test(crop[5:22,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[23:38,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[39:66,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[67:84,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[85:107,95:150],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[120:140,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[140:160,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[160:180,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[175:195,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[190:215,95:150],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[210:230,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[225:250,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[245:265,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[260:285,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[280:300,95:150],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[295:320,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[315:340,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[335:355,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[350:375,95:150],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[370:388,95:150],cnta))

    #Third_column_175-230


    br.append(crop_ans.process_image_and_array_for_test(crop[22:40,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[41:58,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[59:85,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[86:103,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[104:119,175:230],cnta))


    br.append(crop_ans.process_image_and_array_for_test(crop[120:136,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[137:154,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[155:172,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[173:189,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[190:208,175:230],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[210:230,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[225:250,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[245:265,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[260:285,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[280:300,175:230],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[295:320,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[315:335,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[335:355,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[350:370,175:230],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[370:388,175:230],cnta))

    #fourth_column_250-305

    br.append(crop_ans.process_image_and_array_for_test(crop[5:22,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[23:38,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[39:66,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[67:84,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[85:107,250:305],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[100:120,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[120:140,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[140:160,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[160:180,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[180:200,250:305],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[210:230,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[225:250,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[245:265,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[260:285,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[280:300,250:305],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[295:320,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[315:335,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[335:355,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[350:370,250:305],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[370:388,250:305],cnta))

    #fifth_column_325-385

    br.append(crop_ans.process_image_and_array_for_test(crop[5:25,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[25:45,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[45:70,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[65:85,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[80:105,325:385],cnta))


    br.append(crop_ans.process_image_and_array_for_test(crop[120:140,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[140:160,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[160:180,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[175:195,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[190:215,325:385],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[210:230,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[225:245,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[245:265,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[260:285,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[280:300,325:385],cnta))

    br.append(crop_ans.process_image_and_array_for_test(crop[295:316,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[317:332,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[333:348,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[349:367,325:385],cnta))
    br.append(crop_ans.process_image_and_array_for_test(crop[368:385,325:385],cnta))


    
    return np.array(br) , cnta




def crop_img_function():
    crop_img = []

    #for_first_column_20-75

    crop_img.append((20,40,20,75))
    crop_img.append((45,60,20,75))
    crop_img.append((65,80,20,75))
    crop_img.append((85,100,20,75))
    crop_img.append((105,120,20,75))

    crop_img.append((120,136,20,75))
    crop_img.append((137,154,20,75))
    crop_img.append((155,172,20,75))
    crop_img.append((173,192,20,75))
    crop_img.append((193,210,20,75))

    crop_img.append((210,230,20,75))
    crop_img.append((225,250,20,75))
    crop_img.append((245,265,20,75))
    crop_img.append((260,285,20,75))
    crop_img.append((280,300,20,75))

    crop_img.append((300,316,20,75))
    crop_img.append((317,335,20,75))
    crop_img.append((336,352,20,75))
    crop_img.append((353,370,20,75))
    crop_img.append((371,387,20,75))

    #Second_column_95-150

    crop_img.append((5,22,95,150))
    crop_img.append((23,38,95,150))
    crop_img.append((39,66,95,150))
    crop_img.append((67,84,95,150))
    crop_img.append((85,107,95,150))

    crop_img.append((120,140,95,150))
    crop_img.append((140,160,95,150))
    crop_img.append((160,180,95,150))
    crop_img.append((175,195,95,150))
    crop_img.append((190,215,95,150))

    crop_img.append((210,230,95,150))
    crop_img.append((225,250,95,150))
    crop_img.append((245,265,95,150))
    crop_img.append((260,285,95,150))
    crop_img.append((280,300,95,150))

    crop_img.append((295,320,95,150))
    crop_img.append((315,340,95,150))
    crop_img.append((335,355,95,150))
    crop_img.append((350,375,95,150))
    crop_img.append((370,388,95,150))

    #Third_column_175-230


    crop_img.append((22,40,175,230))
    crop_img.append((41,58,175,230))
    crop_img.append((59,85,175,230))
    crop_img.append((86,103,175,230))
    crop_img.append((104,119,175,230))


    crop_img.append((120,136,175,230))
    crop_img.append((137,154,175,230))
    crop_img.append((155,172,175,230))
    crop_img.append((173,189,175,230))
    crop_img.append((190,208,175,230))

    crop_img.append((210,230,175,230))
    crop_img.append((225,250,175,230))
    crop_img.append((245,265,175,230))
    crop_img.append((260,285,175,230))
    crop_img.append((280,300,175,230))

    crop_img.append((295,320,175,230))
    crop_img.append((315,335,175,230))
    crop_img.append((335,355,175,230))
    crop_img.append((350,370,175,230))
    crop_img.append((370,388,175,230))

    #fourth_column_250-305

    crop_img.append((5,22,250,305))
    crop_img.append((23,38,250,305))
    crop_img.append((39,66,250,305))
    crop_img.append((67,84,250,305))
    crop_img.append((85,107,250,305))

    crop_img.append((100,120,250,305))
    crop_img.append((120,140,250,305))
    crop_img.append((140,160,250,305))
    crop_img.append((160,180,250,305))
    crop_img.append((180,200,250,305))

    crop_img.append((210,230,250,305))
    crop_img.append((225,250,250,305))
    crop_img.append((245,265,250,305))
    crop_img.append((260,285,250,305))
    crop_img.append((280,300,250,305))

    crop_img.append((295,320,250,305))
    crop_img.append((315,335,250,305))
    crop_img.append((335,355,250,305))
    crop_img.append((350,370,250,305))
    crop_img.append((370,388,250,305))

    #fifth_column_325-385

    crop_img.append((5,25,325,385))
    crop_img.append((25,45,325,385))
    crop_img.append((45,70,325,385))
    crop_img.append((65,85,325,385))
    crop_img.append((80,105,325,385))


    crop_img.append((120,140,325,385))
    crop_img.append((140,160,325,385))
    crop_img.append((160,180,325,385))
    crop_img.append((175,195,325,385))
    crop_img.append((190,215,325,385))

    crop_img.append((210,230,325,385))
    crop_img.append((225,245,325,385))
    crop_img.append((245,265,325,385))
    crop_img.append((260,285,325,385))
    crop_img.append((280,300,325,385))

    crop_img.append((295,316,325,385))
    crop_img.append((317,332,325,385))
    crop_img.append((333,348,325,385))
    crop_img.append((349,367,325,385))
    crop_img.append((368,385,325,385))
    
    
    return crop_img



def mark_error(exam_sheet,ar,br,crop_img,cnt,x,y):
    
    img = cv2.cvtColor(exam_sheet, cv2.COLOR_GRAY2BGR)
    for i in range(0,100):
        if ar[i] == br[i]:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1],x+crop_img[i][2]:x+crop_img[i][3]],cnt[i][br[i]],-1,(0, 255, 0),4)
        else:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1], x+crop_img[i][2]:x+crop_img[i][3]], cnt[i][br[i]], -1, (0, 0, 255),4)
    
    
    return img
        

def calculate_imgage(ans_sheet,exam_sheet):
    
    # print(ans_sheet)
    
    exam_sheet ,extra_info = crop_sheet(exam_sheet,True)
    

    x, y, w, h = extra_info
    
    ans_result , cnta = meta_calculator(ans_sheet)
    exam_result , cnta = meta_calculator(exam_sheet)
    

    crop_img = crop_img_function()
    
    img = mark_error(exam_sheet,exam_result,ans_result,crop_img,cnta,x,y)

    physics =  np.sum(exam_result[:25] ==  ans_result[:25] )
    chemistry =  np.sum(exam_result[25:40] ==  ans_result[25:40] )
    math =  np.sum(exam_result[40:70] ==  ans_result[40:70] )
    english =  np.sum(exam_result[70:85] ==  ans_result[70:85] )
    analytical =  np.sum(exam_result[85:100] ==  ans_result[85:100] )

    
    
    
    
    return {
        "physics":int(physics),
        "chemistry":int(chemistry),
        "math":int(math),
        "english":int(english),
        "analytical":int(analytical),
    } , img

