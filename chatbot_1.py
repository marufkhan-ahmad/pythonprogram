
from urllib import response
from flask import render_template, request
import nltk
from nltk.chat.util import Chat
qa_pairs =[["Hello",["Hi how can i help you"]],
["good morning",["good morning too do you want to know the plan of this firm"]],
["what's your name",["my name is khan"]],
["nice to meet you mr khan",["nice to meet you too"]],
["Can you drop your contact number here",["yes sure 8809162229"]],
["(.*)(location|city|address) ?",["Address: E-16/1 SL Kumbha marg"]],
["(.*)contact(.*)",["Call- 8809162229 or you can visit"]],
["(.*)weather(.*)",["it is too hot let's talk on call instead of visit"]]


]
cb = Chat(qa_pairs)
cb.converse()       
