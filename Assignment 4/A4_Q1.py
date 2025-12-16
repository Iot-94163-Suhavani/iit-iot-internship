def km_to_m(km):
    return km*1000
def m_to_cm(m):
    return m*100
def cm_to_mm(cm):
    return cm*10
def feets_to_inches(feets):
    return feets*12
def inches_to_cm(inches):
    return inches*2.54
def dis_conv(distance,conversion_type,func):
    result=func(distance)
    print(f"{conversion_type}:{result}")
    
distance=float(input("Enter distance: "))

dis_conv(distance,"kilometer to meter",km_to_m)
dis_conv(distance,"meter to centimeter",m_to_cm)
dis_conv(distance,"centimeter to millimeter",cm_to_mm)
dis_conv(distance,"feets to inches",feets_to_inches)
dis_conv(distance,"inches to centimeter",inches_to_cm)