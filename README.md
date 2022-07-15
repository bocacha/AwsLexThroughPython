## AWS Lex V2Bot 

An alternative approach to build a functional AWS Lex bot.
It making use of Python files, instead of Terraform files that only allow to build a Version1 Lex.
The project was made on Linux Environment ( Ubuntu 20)

### Walkthrought:

*   Install pip from the console with the following command:

$ sudo apt install python3-pip

*   Install Boto3 :

$ pip install boto3

*   You can switch to branch querystudents to see an more advanced example

*   Then, execute the command that build every one of the needed modules:

$python3 create.py
$python3 createversion.py
$python3 createlocale.py
$python3 intent.py
$python3 slot.py
$python3 slotType.py

Or for the advanced bot:

$python3 createbot.py
$python3 createbotversion.py
$python3 createbotlocale.py
$python3 welcome.py
$python3 querystudents.py
$python3 bootcampType.py
$python3 nationalityType.py
$python3 welcomeslot.py
$python3 bootcampslot.py
$python3 nationalityslot.py



