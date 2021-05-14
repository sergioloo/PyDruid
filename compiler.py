import json
import os
from utils.error import Error


class Compiler:
    def __init__(self, proj_name, source_code):
        self.source_code    = source_code
        self.proj_idx       = None

        self.project_name   = proj_name
        self.compiler       = ''
        self.output         = ''
        self.flags          = ''
        self.command        = ''

        self.load_idx()
    
    def load_idx(self):
        with open(f'{self.project_name}/project.json', 'r') as proj_idx_f:
            self.proj_idx = json.load(proj_idx_f)

        try:
            self.compiler   = self.proj_idx['compiler']
            self.flags      = self.proj_idx['flags']
            self.command    = self.proj_idx['com']

            self.output     = f"{self.project_name}/{self.proj_idx['output_file']}"

        except:
            Error("invalid project index.")

    def compile(self, clean=True):
        c_source_fn = f'{self.project_name}/{self.project_name}.dout.c'

        with open(c_source_fn, 'w') as c_source_f:
            c_source_f.write(self.source_code)

        command = self.command.replace('{compiler}', self.compiler)
        command = command.replace('{dsrc}', c_source_fn)
        command = command.replace('{output_file}', self.output if self.output != '' else self.project_name)
        command = command.replace('{flags}', self.flags)

        compilation_status = os.system(command)

        if compilation_status == 0: print(f'\x1b[1m· \x1b[mcompilation \x1b[1;32msuccessful\x1b[m.')
        else: print(f'\x1b[1m· \x1b[mcompilation \x1b[1;31mfailed\x1b[m.')

        if clean: os.remove(c_source_fn)

        return compilation_status
