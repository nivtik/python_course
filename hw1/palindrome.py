def palindrome_tester(str_num):
    if str_num==str_num[::-1]:
        return True
    else:
        return False

def check_palindrome():
    palindrome_list=[]
    for number in range(100000,1000000):
        str_number=str(number)
        last4=str_number[2:6]
        if palindrome_tester(last4):
           number2=number+1
           str_number2=str(number2)
           last5=str_number2[1:6]
           if palindrome_tester(last5):
               number3=number2+1
               str_number3=str(number3)
               middle4=str_number3[1:5]
               if palindrome_tester(middle4):
                   number4=number3+1
                   str_number4=str(number4)
                   if palindrome_tester(str_number4):
                       palindrome_list.append(number)

    return palindrome_list

palindrome_list=check_palindrome()
print(palindrome_list)


