import math


fencing_per_metre = 75
grass_per_square_metre = 20
major_radius = 10
minor_radius = 5

area = int(round(math.pi*major_radius*minor_radius))
perimeter = int(round(2*math.pi*math.sqrt((major_radius*major_radius+minor_radius*minor_radius)/2)))
print('*'*50)
print('Cost of laying grass (',area,' square meters): $',area*grass_per_square_metre,sep='')
print('Cost of fencing (',perimeter,' meters): $',perimeter*fencing_per_metre,sep='')
print('Total cost: $',area*grass_per_square_metre+perimeter*fencing_per_metre,sep='')
print('*'*50)