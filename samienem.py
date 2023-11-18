def describe():
    print("Describe yourself in brief")

if __name__=="__main__":
    describe()


print(__name__)        # name output dega ki ye kaha se print/run ho rha hai

# aur agr name ki value/output main h mtlb isko yhi se run kiya ja rha hai aur agr isko kahi aur se run krenge to waha iss file ka naam aayega (that is here samienem) 
# aur agr isko yaha se run kiya ja rha hai to describe ko run krega but agr kahi aur se run krenge to describe ko run nhi krna hai this can be done by using below code
#      if __name__=="__main__"



# we can check that the program is in __main__ or not by using print(__name__) and we should check it as bcoz may some could harm your computer or other things in the computer so we check it before running it.