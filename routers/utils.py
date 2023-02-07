import re


def validate_email(email) -> bool:
  email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

  if(re.search(email_regex, email)):  
      return True  
  else:  
      return False  
