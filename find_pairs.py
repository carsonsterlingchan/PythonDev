# This is a mock interview question presented in an Udemy course - Python For Algorithms, Data Structures and Interviews.
# Instructor is Jose Portilla.

# Original Problem:
# Given a list of integers and a target number, write a function that returns a boolean indicating
# if its possible to sum two integers from the list to reach the target number.

# Original Requirement:
# You can not use an integer element twice. Optimize for time over space

# I changed his problem.  This function prints out pairs of integers that match the target number.
# I also enhanced the solution that he provided in the course.

# input: [1,2,4,3,5,6] 6
# output:
# (1,5)
# (2,4)


def find_pairs(lst, the_sum):
    
    if len(lst) == 0:
        raise Exception('List needs at least 2 integers')
    
    # Make sure the list is sorted.  This is important
    # Otherwise, numbers will not printed in pairs.
    
    lst.sort()
    
    seen1 = []
    seen2 = []
    
    for num in lst:
        
        diff = the_sum - num
        
        if diff in seen1:
            seen2.append(diff)
        else:
            seen2.append(0)
        
        seen1.append(num)
        
    for i in range(len(seen1)-1, -1, -1):
        
        if seen2[i] != 0:
            print '({0},{1})'.format(seen2[i], seen1[i])
    

if __name__ == '__main__':
    a_list = [1,2,3,4,5]
    target_num = 6
    print 'List is: {0}, Target Number is: {1}'.format(a_list, target_num)
    print 'Results is:'
    find_pairs(a_list, target_num)
