__module_name__ = 'Twitch garbage'
__module_version__ = '0.2'
__module_description__ = 'Remove annoying garbage messages'
__module_author__ = 'Kibur'

import hexchat

def format(string):
	string = '\002\035' + string
	hexchat.prnt(string)

def clearchat(word, word_eol, userdata):
	if word[1] == 'CLEARCHAT' and len(word) == 4:
		format(word[3].replace(':', '', 1) + ' has been timed out.')
	elif word[1] == 'CLEARCHAT' and len(word) == 3:
		format('Chat has been cleared.')
	else:
		return hexchat.EAT_NONE

	return hexchat.EAT_ALL

def whisper(word, word_eol, userdata):
	whisper = word_eol[3].replace(':', '', 1)
	user = word[0].split('!')[0].replace(':', '', 1)
	format(user + ' whispers to you: ' + whisper)

	return hexchat.EAT_ALL

def userstate(word, word_eol, userdata):
	return hexchat.EAT_ALL

def unload_cb(userdata):
	hexchat.prnt('\003' + __module_name__ + ' ' + __module_version__ + ' unloaded\003')

hexchat.hook_server('CLEARCHAT' ,clearchat)
hexchat.hook_server('WHISPER' ,whisper)
hexchat.hook_server('USERSTATE' ,userstate)

hexchat.prnt('\003' + __module_name__ + ' ' + __module_version__ + ' loaded\003')
