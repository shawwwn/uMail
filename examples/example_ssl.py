#
# An example for sending a long email
# with SSL connection
#
# NOTE:
# If the email is too long to fit in an variable,
# you may use write() to send a chunk of the email 
# each time.
#

import umail
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login('bob@gmail.com', 'bobspassword')
smtp.to('alice@gmail.com')
smtp.write("From: Bob <bob@gmail.com>\n")
smtp.write("To: Alice <alice@gmail.com>\n")
smtp.write("Subject: Poem\n\n")
smtp.write("Roses are red.\n")
smtp.write("Violets are blue.\n")
smtp.write("...\n")
smtp.send()
smtp.quit()
