""" 

""" 
from javax.swing import JFrame;
from javax.swing import JFileChooser;
from javax.swing import JOptionPane
from org.parosproxy.paros.model import Model
import json


def get_context_name():
	ctx_name = JOptionPane.showInputDialog(None, "Enter a Name for the Context")
	return ctx_name

def get_file_name():
	frame = JFrame("Filename")
	frame.setLocation(100,100)
	frame.setSize(500,400)
	frame.setLayout(None)
	fc = JFileChooser()
	result = fc.showOpenDialog(frame)
	if not result == JFileChooser.APPROVE_OPTION:
		return None
	file_name = fc.getSelectedFile()
	return file_name

def get_url_regexes(file_name):
	with open(file_name, "r") as f:
		data = json.load(f)
	includes = data['target']['scope']['include']
	regexes = []
	for include in includes:
		regexes.append(include['host'])
	return regexes

def create_new_context(ctx_name):
	session = Model().getSingleton().getSession()
	new_context = session.getNewContext(ctx_name)
	return new_context

def populate_context(url_regexes, context):
	for pattern in url_regexes:
		context.addIncludeInContextRegex(pattern)

ctx_name = get_context_name()
file_name = get_file_name()
ctx = create_new_context(ctx_name)
url_regexes = get_url_regexes(str(file_name))
populate_context(url_regexes, ctx)
