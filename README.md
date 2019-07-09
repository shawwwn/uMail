# µMail (MicroMail)
A lightweight, scalable SMTP client for sending email in MicroPython.


## Usage:

A bare minimal approach

```py
import umail
smtp = umail.SMTP('smtp.gmail.com', 587, username='my@gmail.com', password='mypassword')
smtp.to('someones@gmail.com')
smtp.send("This is an example.")
smtp.quit()
```


## API docs:

* **`umail.SMTP(host, port, [ssl, username, password])`**
  * **host** - smtp server
  * **port** - server's port number
  * **ssl** - set `True` when SSL is required by the server
  * **username** - my username/email to the server
  * **password** - my password

* **`SMTP.login(username, password)`**
  If you did not login when intializing the server, do it here!

* **`SMTP.to(addrs, mail_from)`**
  * **addrs** - Recipient's email address. If multiple recipents, use a list, eg. `['aaa@mail.com', 'bbb@mail.com']`
  * **mail_from** - manually specify the MAIL FROM address, default value is your smtp username. [example](examples/example_mail_from.py)

* **`SMTP.write(content)`**
  To send a long email or an email that contains large attachments, you will most likely exceed the memory limit of your MCU.\
  Use this function to break up your email into smaller chunks.\
  Each call to `write()` will cause the current `content` to be sent to the server so you can load the next chunk.

* **`SMTP.send([content])`**
  Finish writing the email.\
  Make the SMTP server to actually send your email to the recipent address.

* **`SMTP.quit()`**
  Close the connection to the server


## Other

For more details, pleasse refer to sample code under `examples\`
