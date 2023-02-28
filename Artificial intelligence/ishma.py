import math

def calculate_Beam(dim_of_slab):
    depth = (dim_of_slab * 12) / 18
    breadth = depth / 3
    if breadth < 12:
        breadth = 12
    print("Depth = "+str(depth))
    print("Breadth = "+str(breadth))
    return math.ceil(breadth/2.) * 2

def calculate_Column_Dimension(beam):
    col = beam * 1.1
    print("Column = "+str(math.ceil(col/2.)*2))
    number_of_stories = int(input("Enter number of stories: "))
    print("Number of stories in building = "+str(number_of_stories))
    c_area = (1.1**number_of_stories * beam)**2
    return c_area

#slab thickness
def slab_thickness(dim_of_slab, col_area):
    thickness = dim_of_slab / (33 * 12)
    print("The thickness of slab = " + str(thickness))
    area_of_bar = (col_area * 2) /100
    print("The area of steel bar = " + str(area_of_bar))
    no8_bar = area_of_bar / 0.79
    return math.ceil(no8_bar/2.)*2

dim_of_slab = int(input("Enter number: "))
print("The dimension of slab = "+str(dim_of_slab))
beam = calculate_Beam(dim_of_slab)
print("The beam of slab = "+str(beam))
col_area = calculate_Column_Dimension(beam)
print("The dimension of column = "+str(col_area))
num8_bar = slab_thickness(dim_of_slab, col_area)
print("The size of #8 bar = "+str(num8_bar))

