#LAB ASSIGNMENT -1
# created by SSDK

## QUESTION - 1

#function for password check
def pswd_chk():
 #if the given return value is true, while loop is executed!
 while True:
  in_pswd = input('Input Your Desired Password : ')
  n = len(in_pswd)
  if n < 6:
    print('Password length at least 6 letters')
  elif n > 16:
    print('Password length should not exceed 16 letters')
  elif not any(each_letter.isdigit() for each_letter in in_pswd):
    print('Password must have at least one Numeric value')
  elif not any(each_letter.isupper() for each_letter in in_pswd):
    print('Password must have at least one Uppercase letter')
  elif not any(each_letter.islower() for each_letter in in_pswd):
    print('Password must have at least one Lowercase letter')
  elif not any(each_letter in Spl_Char for each_letter in in_pswd):
    print('Password must have at least one Special Characters among $@!*')
    val_chk=False
  #if password satisfy the given requirements, password is accepted
  else:
    print('Success! Your Password meets the requirements.')
    break
 return print("Your password is "+ in_pswd)

#Source - Initialization
#special characters are initialized
Spl_Char=['$','@','!','*']
val_chk=True
#function is declared here which iterates untill correct password is set.
pswd_chk()

