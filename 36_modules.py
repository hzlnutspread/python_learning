# module = a file that contains python code. May contain functions, classes etc
# Used with modular programming, which is to separate a program into parts

# Say we have another module called "messages"
# to import that module of functions, classes etc, we will type the following:

import messages

# in order to use functions:
messages.hello()
messages.bye()


# to shorten things we can do this instead:
import messages as msg

msg.hello()
msg.bye()


# can even do this
from messages import hello, bye

hello()
bye()


# to see a list of modules available
help("modules")
