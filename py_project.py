import math

ax = float(raw_input("Ax="))
ay = float(raw_input("Ay="))
bx = float(raw_input("Bx="))
by = float(raw_input("By="))

theta = math.atan2(ay, ax) - math.atan2(by, bx)
print "theta=" + str(theta)

da = math.sqrt(ax*ax + ay*ay)
db = da * math.cos(theta)

thetab = math.atan2(by, bx)
px = db * math.cos(thetab)
py = db * math.sin(thetab)

print "(" + str(px) + "," + str(py) + ")"
