History={'Subject': 'History','James': [100,93], 'Monica': [99,97], 'Reggie': [73,99], 'Jenn': [54,91], 'Albert': [44,100]}
Math={'Subject': 'Math','James': [55,91], 'Monica': [77,66], 'Reggie': [86,92],'Mike':[33,99], 'Jenn': [64,98],}
Result={}
def compare_subjects_within_student(subj1,subj2):
    for name in subj1:
        if type(subj1[name]) is list:
            if name in subj2:
                sum_subj_1=subj1[name][0]+subj1[name][1]
                mean_subj_1=sum_subj_1/2
                sum_subj_2 = subj2[name][0] + subj2[name][1]
                mean_subj_2 = sum_subj_2 / 2
                if mean_subj_1>=mean_subj_2:
                    Result[name]= subj1['Subject']
                else:
                    Result[name]= subj2['Subject']
    return Result

Result=compare_subjects_within_student(History,Math)
print(Result)

