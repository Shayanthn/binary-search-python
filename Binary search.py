def dodoee (arr,target):
    left = 0 #hamishe 0 chon index aval 0 
    right = len(arr) - 1 #akharin addad ro neshoon mide -1 ham chon index az 0 shoroo shude 
    while left <= right : #age left bozorgtar bashe dige addadi nist baraye search !
        mid = (left+right) // 2
        if arr[mid] == target : #arr[mid] aval mid ro hesab mikone bad index mishe meqdar vasat 
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid - 1 
    return -1
nummbers = []
print("LOTFAN 20 ADAD VARED KONID : ")
for i in range (20) : 
    num = int(input(f"adad : {i+1} : "))
    nummbers.append(num)
    nummbers = sorted(nummbers)
print(nummbers)
target = int(input("adad mored nazar baraye jostejoo : "))
index = dodoee(nummbers,target)
if index != -1 : ## != yany inequality
    print(f" adad \n{target} vojood darad dar index \n{index}") ##hatman f bashe ta reshte kham beshe \n ye kat miyare paiin
else : 
    print(f"\n no found !")
    
## https://github.com/Shayanthn
## shayanthn78@gmail.com
""" 🚀 About the Developer
Python Expert | Advanced English Instructor | Creative Thinker

Passionate Python developer with expertise in web development, AI, automation, and data science. Skilled in problem-solving, clean code, and scalable solutions. Also an advanced English instructor with strong communication and technical documentation abilities.

💡 Innovator & Idea Generator | Always seeking to create efficient, cutting-edge projects.
📌 Proficient in Django, Flask, FastAPI, TensorFlow, Pandas, Selenium, and more.
🚀 Open to collaboration on GitHub and tech-driven projects.
 """



    
        
