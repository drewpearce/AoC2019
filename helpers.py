from functools import reduce
from operator import mul
import os
import time


def load_inputs_lines(folder, file_name, out_type=None):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        folder,
        file_name
    )
    with open(path) as f:
        out = f.readlines()

    if out_type == 'int':
        out = [int(o) for o in out]

    return out


class IntcodeComputer(object):
    def __init__(self, instructions, inputs=None):
        self.instructions = instructions
        self.inputs = inputs
        self.output = []
        self.ptr = 0
        self.param_lengths = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0
        }

    def add(self, params):
        params[2] = (1, params[2][1])
        params = self.get_param_vals(params)
        self.instructions[params[2]] = sum(params[:2])
        self.ptr += 4

    def multiply(self, params):
        params[2] = (1, params[2][1])
        params = self.get_param_vals(params)
        self.instructions[params[2]] = reduce(mul, params[:2], 1)
        self.ptr += 4

    def save_in(self, params):
        self.instructions[params[0][1]] = self.inputs
        self.ptr += 2

    def save_out(self, params):
        params = self.get_param_vals(params)
        self.output.append(params[0])
        self.ptr += 2

    def jump_if_true(self, params):
        params = self.get_param_vals(params)
        if params[0] != 0:
            self.ptr = params[1]
        else:
            self.ptr += 3

    def jump_if_false(self, params):
        params = self.get_param_vals(params)
        if params[0] == 0:
            self.ptr = params[1]
        else:
            self.ptr += 3

    def less_than(self, params):
        params[2] = (1, params[2][1])
        params = self.get_param_vals(params)
        if params[0] < params[1]:
            self.instructions[params[2]] = 1
        else:
            self.instructions[params[2]] = 0

        self.ptr += 4

    def equals(self, params):
        params[2] = (1, params[2][1])
        params = self.get_param_vals(params)
        if params[0] == params[1]:
            self.instructions[params[2]] = 1
        else:
            self.instructions[params[2]] = 0

        self.ptr += 4

    def get_param_vals(self, params):
        return [self.get_val(p) for p in params]

    def get_val(self, param):
        if not isinstance(param, tuple):
            raise Exception('get_val method takes a tuple')

        if param[0] == 0:
            return self.instructions[param[1]]
        elif param[0] == 1:
            return param[1]
        else:
            return None

    def get_code_params(self, instr_set):
        code = int(str(instr_set[0])[-2:])
        p_modes = str(instr_set[0])[:-2]

        while len(p_modes) < self.param_lengths[code]:
            p_modes = '0' + p_modes

        modes = reversed([int(i) for i  in p_modes])

        params = []
        for i, m in enumerate(modes):
            params.append((m, instr_set[i + 1]))

        return code, params

    def run(self):
        func_map = {
            1: self.add,
            2: self.multiply,
            3: self.save_in,
            4: self.save_out,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals
        }

        while self.ptr < len(self.instructions):
            code, params = self.get_code_params(self.instructions[self.ptr:])

            if code == 99:
                break
            elif code not in func_map:
                raise Exception(f'Code {code} not a valid op code.')

            func_map[code](params)


class Timer(object):
    def __init__(self):
        self.start_time = self.now()
        self.stop_time = None
        self.duration = None

    @staticmethod
    def now():
        return int(round(time.time() * 1000))

    def start(self):
        self.start_time = self.now()
        self.stop_time = None
        self.duration = None

    def stop(self):
        self.stop_time = self.now()
        self.duration = self.stop_time - self.start_time
