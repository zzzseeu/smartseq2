
class Template:
    def __init__(self, inputs, output, args):
        self.inputs = inputs
        self.output = output
        self.args = args

    def process_input(self):
        raise NotImplementedError("Please implement the process_input method")
    
    def process_output(self):
        raise NotImplementedError("Please implement the process_output method")
    
    def process_args(self):
        raise NotImplementedError("Please implement the process_args method")
    
    def run(self):
        raise NotImplementedError("Please implement the run method")