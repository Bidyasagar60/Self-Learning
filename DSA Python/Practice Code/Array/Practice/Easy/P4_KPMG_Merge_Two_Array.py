
"""
Write a Python program to merge two lists element-wise, assuming they have the same length.

"""

if __name__ == '__main__':

    student_IDs=[101, 102, 103]
    student_Names=["Alice", "Bob", "Charlie"]
    Merged_List=[]
    for i in range(len(student_IDs)):

        Merged_List.append((student_IDs[i],student_Names[i]))

    print(Merged_List)