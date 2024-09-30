from src.common.template import Template

class QC(Template):
    def __init__(self, step_name, inputs, outdir, args):
        super().__init__(step_name, inputs, outdir, args)

    def process_input(self, fastq1, fastq2, adaptor, min_quality, min_length):
         pass

    def process_args(self):
        return super().process_args()
    
    def process_output(self):
        return super().process_output()
    
    def run(self):
        return super().run()
    
