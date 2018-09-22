#
# An bare minimium example for sending a email
# without SSL connection
#

import umail
smtp = umail.SMTP('smtp.gmail.com', 587, username='my@gmail.com', password='mypassword')
smtp.to('someones@gmail.com')
smtp.send("This is an example.")
smtp.quit()
