import threading
import subprocess
import time
import socket

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper


class StanfordCoreNLPServer():


    def __init__(self, corenlp_dir):
        self.corenlp_dir = corenlp_dir


    @threaded
    def _run_server(self):
        command = 'java -mx5g -cp "'+self.corenlp_dir+'"  edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000'
        p = subprocess.Popen(
            command,
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    def run(self):
        if self._is_port_open(9000):
            thread = self._run_server()
            time.sleep(1)
            #logging.debug("run a new server")
        else:
            print("dd")
            #logging.debug("using the server")



    def _is_port_open(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False
        try:
            sock.bind(("0.0.0.0", port))
            result = True
        except:
            #logging.exception("Port is in use")
            print("d")
        sock.close()
        return result





