m=lambda km:km*1000
cm=lambda m:m*100
mm=lambda cm:cm*10
inches=lambda feets:feets*12
i_to_cm=lambda inches:inches*2.54

dis=float(input("Enter distance :"))

print(f"km_to_m={m(dis)}")
print(f"m_to_cm={cm(dis)}")
print(f"cm_to_mm={mm(dis)}")
print(f"feets_to_inches={inches(dis)}")
print(f"inches_to_cm={i_to_cm(dis)}")