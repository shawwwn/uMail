#
# Setting the MAIL FROM address
#
# Some services may require you to set the MAIL FROM address different than your 
# login username. In such cases, you can manually specify the address by
# smtp.to(mail_from=address)
# If argument not set, MAIL FROM address will be default to your login username.
#
# Read more about MAIL FROM:
# https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html
#

import umail
smtp = umail.SMTP('email-smtp.us-west-2.amazonaws.com', 587, username='myusername', password='mypassword')
smtp.to('someones@gmail.com', mail_from='my@gmail.com')
smtp.send("This is an example.")
smtp.quit()
