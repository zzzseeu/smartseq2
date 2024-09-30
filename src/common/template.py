import os
from functools import lru_cache


class Template:
    def __init__(self, step_name, inputs, outdir, args):
        self.step_name = step_name
        self.inputs = inputs
        self.outdir = outdir
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        self.args = args

    @lru_cache(maxsize=None)
    def process_input(self):
        raise NotImplementedError("Please implement the process_input method")
    
    @lru_cache(maxsize=None)
    def process_output(self):
        raise NotImplementedError("Please implement the process_output method")
    
    @lru_cache(maxsize=None)
    def process_args(self):
        raise NotImplementedError("Please implement the process_args method")
    
    @lru_cache(maxsize=None)
    def run(self):
        raise NotImplementedError("Please implement the run method")