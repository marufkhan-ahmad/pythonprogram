import nltk
from nltk.chat.util import Chat
# To create an empty list
qa_pairs = [["(.*)name", ["My name is upbot"]], ["what is your favourite food",["Sorry i can't eat"]],[("hi||Hi||hey||Hey"),["hello how can i help you" ]]
 

     ]
cb = Chat(qa_pairs)
cb.converse()
cb.respond("what is your favourite food")