def calculate_average(student_data):
    # return avg 
    avgmark = (int(student_data[2]) + int(student_data[3]) + int(student_data[4])) / 3
    return round(avgmark, 2)  # Round to 2 decimal so no error coe
