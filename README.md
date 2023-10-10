# AirBnB_clone

## Description of the project.
The goal of the project is to deploy on a server a simple copy of the
[AirBnB website](https://www.airbnb.com/).

Only some of the features to cover all fundamental concepts of the higher level
programming track will be implemented.

At this stage, this project will compose of a command interpreter to manipulate
data without a visual interface, like in a Shell (perfect for development and
debugging).

### Concepts used
- [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
- [Python package](https://intranet.alxswe.com/concepts/66)
- [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
- [Unittest](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- Serialization/Deserialization
- [\*args, \**kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
- [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)

## Description of the command interpreter:
### How to start it
#### The console
- create data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

### How to use it
- Clone the repo to your local machine throught its link;
```bash

git clone https://github.com/Fawazabdganiyu/AirBnB_clone.git

```

- Make the `console.py` file executable;
```bash

chmod u+x console.py

```
- Then run the command.
```bash

./console.py

```

### Examples
#### Execution
*The shell would work like this in interactive mode:*
```bash

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```
*And also in non-interactive mode: (like the Shell project in C)*
```bash

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

```