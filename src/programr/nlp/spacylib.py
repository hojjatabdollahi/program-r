import spacy
from programr.utils.logging.ylogger import YLogger

spacy_lib = spacy.load("en")
YLogger.info(None, "spacy model loaded")