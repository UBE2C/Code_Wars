import copy
import re
from typing import TypedDict

class EnvDict(TypedDict):
    names: list[str]
    envs: list[list[str]]

class Pattern:
    def __init__(self, name: str, value: list[str], local_scope: str, parent_scope: list[str] = []) -> None:
        self.name: str = name
        self.value: list[str] = value
        self.local_scope: str = local_scope
        self.parent_scope: list[str] = parent_scope

    def __str__(self) -> str:
        return f"Pattern {self.name}: \ninstructions: < {self.value} >\n< local_scope: {self.local_scope} >\n< parent_scope: {self.parent_scope} >"

    def __repr__(self) -> str:
        return self.__str__()


class RSUProgram:
    def __init__(self, code: str) -> None:
        self.code: str = code
        self.orientation: str = "E"
        self.x_position: int = 0
        self.y_position: int = 0
        self.token_lst: list[str] = []
        self.instruction_lst: list[str] = []
        self.pattern_lst: list[Pattern] = []
        self.pattern_envs: EnvDict = {"names" : [], "envs" : []}
        self.env_stack: list[str] = ["global"]
        self.path: dict[str, list[int]] = {"x_coords" : [], "y_coords" : []} #for simple access to min/max values
        self.coord_lst: list[list[int]] = [] #to store the x/y coord pairs
        self.direction_lst: list[str] = [] #to store the direction the movement happened
        self.loop_map: dict[int, int] = {}
        self.pattern_map: dict[int, int] = {}
        self.call_stack: list[int] = []
        self.output_list: list[str] = []
        #self.update_path(x = self.x_position, y = self.y_position)
        self.path_map: str = ""
        

    def __repr__(self) -> str:
        return f"A robot which is facing <{self.orientation}>, and its position is <{self.x_position}, {self.y_position}>."
    
    def __str__(self) -> str:
        return self.__repr__()


    def get_tokens(self) -> None:
        input_code: str = self.code
        code_lst: list[str] = input_code.split("\n")
        clean_code_lst: list[str] = []

        lp: int = 0
        while lp < len(code_lst):
            line: str = code_lst[lp]
            line: str = line.strip()

            if lp + 1 < len(code_lst):
                next_line: str = code_lst[lp + 1]
            else:
                next_line: str = ""
            
            next_line.strip()
            
            if line.startswith("//"):
                pass

            elif line.find("//") != -1:
                if len(next_line) != 0 and next_line[0].isnumeric():
                    raise SyntaxError(f"tokenizer: at position {lp} a comment should not be followed by a numeric value.")

                clean_line: str = line.split("//", 2)[0]

                if clean_line.find("/*") != -1:
                    comment_start: int = line.find("/*")
                
                    if clean_line.find("*/") != -1:
                        comment_end: int = clean_line.find("*/") + 2 #to jump tp the next character after the comment

                        if clean_line[comment_end].isnumeric():
                            raise SyntaxError(f"tokenizer: at position {comment_end} a comment should not be followed by a numeric value.")

                    else:
                        comment_end: int = len(clean_line)

                    clean_line: str = clean_line[slice(0, comment_start)] + clean_line[slice(comment_end, len(clean_line))]

                if len(clean_line) > 0:
                    clean_code_lst.append(clean_line)

            elif line.startswith("/*") and line.find("*/") == -1:
                sub_lp: int = lp
                while sub_lp < len(code_lst):
                    if code_lst[sub_lp].endswith("*/"):
                        break

                    sub_lp += 1
    
                lp = sub_lp

            elif line.find("/*") != -1:
                comment_start: int = line.find("/*")
                
                if line.find("*/") != -1:
                    comment_end: int = line.find("*/") + 2 #to jump tp the next character after the comment

                    if comment_end < len(line) and line[comment_end].isnumeric():
                        raise SyntaxError(f"tokenizer: at position {comment_end} a comment should not be followed by a numeric value.")

                else:
                    comment_end: int = len(line)

                clean_line: str = line[slice(0, comment_start)] + line[slice(comment_end, len(line))]

                if clean_line.startswith("//"):
                    pass

                elif len(clean_line) > 0:
                    clean_code_lst.append(clean_line)

            elif line.find("*/") != -1:
                comment_end: int = line.find("*/") + 2

                if line[comment_end].isnumeric():
                    raise SyntaxError(f"tokenizer: at position {comment_end} a comment should not be followed by a numeric value.")

                clean_line: str = line[slice(comment_end, len(line))]

                if len(clean_line) > 0:
                    clean_code_lst.append(clean_line)

            else:
                    clean_code_lst.append(line)

            lp += 1


        code: str = ""
        for line in clean_code_lst:
            code += line


        cp: int = 0
        while cp < len(code):
            instr: str = code[cp]
            
            if cp + 1 < len(code):
                next_instr: str = code[cp + 1]
            
            else:
                next_instr: str = ""

            if cp == 0 and instr.isnumeric():
                    raise SyntaxError(f"tokenizer: at position {cp} a numeric value {instr} was found, but is not allowed.")

            if instr == "F" or instr == "R" or instr == "L" or instr == ")":
                if next_instr.isnumeric():
                    sub_cp: int = cp + 1
                    repeat: str = ""
                    while sub_cp < len(code) and code[sub_cp].isnumeric():
                        repeat += code[sub_cp]
                        sub_cp += 1

                    if len(repeat) > 1 and repeat.startswith("0"):
                        raise SyntaxError(f"tokenizer: at position {cp} a repeat value starts with 0 {repeat} which is not allowed.")

                    self.token_lst.append(instr + repeat)
                    cp = sub_cp - 1
                
                else:
                    self.token_lst.append(instr)

            elif instr == "(":
                self.token_lst.append(instr)

            elif instr == "p" or instr == "P":
                if not next_instr.isnumeric():
                    raise SyntaxError(f"tokenizer: at position {cp} a pattern declaration must be followed by a numeric value, instead {code[cp + 1]} was found.")
                
                elif cp == len(code) - 1:
                    raise SyntaxError(f"tokenizer: at position {cp} a pattern declaration must be followed by a numeric value, but none was found.")
                
                elif next_instr.isnumeric():
                    sub_cp: int = cp + 1
                    id: str = ""
                    while sub_cp < len(code) and code[sub_cp].isnumeric():
                        id += code[sub_cp]
                        sub_cp += 1

                    self.token_lst.append(instr + id)
                    cp = sub_cp - 1

                    if len(id) > 1 and id.startswith("0"):
                            raise SyntaxError(f"tokenizer: at position {cp} a repeat value starts with 0 {id} which is not allowed.")
                
                else:
                    self.token_lst.append(instr)

            elif instr == " ":
                if cp < len(code) and next_instr.isnumeric():
                    raise SyntaxError(f"tokenizer: at position {cp} a space is followed by a numeric value {code[cp + 1]} which is not allowed.")
                
                else:
                    pass
                
            elif instr == "q":
                self.token_lst.append(instr)
            
            else:
                raise SyntaxError(f"tokenizer: at position {cp}, an unsupported value {instr} was found.")

            
            cp += 1

        return self.token_lst


    def map_loops(self, token_list: list[str], sub_loop: bool = False) -> None | dict[int, int]:
        tokens: list[str] = token_list
        stack: list[int] = []
        current_map: dict[int, int] = {}


        for i, token in enumerate(tokens):
            if token == "(":
                stack.append(i)

            if token == ")" or re.match("[)][0-9]+", token):
                loop_start: int = stack.pop()
                current_map[loop_start] = i #forward map
                current_map[i] = loop_start #reverse map

        if sub_loop == False:
            self.loop_map = current_map

            return None
        
        else:
            return current_map

    def map_patterns(self) -> None:
        if len(self.pattern_map) == 0:
            tokens: list[str] = self.token_lst
            stack: list[int] = []
            pattern_map: dict[int, int] = {}

            for i, token in enumerate(tokens):
                if re.match(pattern = "p[0-9]+", string = token): #This will only eval true if the token matches the pattern
                    stack.append(i)

                if token == "q":
                    pattern_start: int = stack.pop()
                    pattern_map[pattern_start] = i #forward map
                    pattern_map[i] = pattern_start #reverse map

            self.pattern_map = pattern_map

    def map_pattern_envs(self) -> None:
        #Transfer ownership
        pattern_list: list[Pattern] = copy.deepcopy(self.pattern_lst)

        if len(self.pattern_envs["names"]) == 0:
            for pat in pattern_list:
                self.pattern_envs["names"].append(pat.name)
                self.pattern_envs["envs"].append(pat.parent_scope)


    def replace_pattern_call(self, input_instruction_list: list[str], output_instruction_list: list[str]) -> None:
        #Transfer input list ownership
        inst_lst: list[str] = copy.deepcopy(input_instruction_list)
        envs: EnvDict = copy.deepcopy(self.pattern_envs)

        lp: int = 0
        while lp < len(inst_lst):
            token: str = inst_lst[lp]

            if re.match(pattern = "[P][0-9]+", string = token):
                self.call_stack.append(lp)
                
                #Define max recursion depth
                if len(self.call_stack) > 20:
                    raise RecursionError(f"execute: a pattern {token} has exceeded the maximum recursion depth.")

                #Check if the called pattern is defined
                if token not in envs["names"]:
                    raise ValueError(f"execute: the pattern {token} is not defined.")
                
                #Pull out the indices for every matching pattern from the pattern_env map
                matching_pattern_indices: list[int] = []
                for i, name in enumerate(envs["names"]):
                    if name == token:
                        matching_pattern_indices.append(i)

                #Pull out the definition environment paths for the matching patterns
                definition_envs: list[list[str]] = [envs["envs"][_] for _ in matching_pattern_indices]
                
                #Compare the env paths of the matching patterns to the caller env path and see if it can reach any of the matching patterns
                match_found: bool = False #break condition
                call_index: int = 0 #the index of the matching pattern which is reachable for the caller
                
                for i, env in enumerate(definition_envs): #Direct call env matching
                    if len(env) < len(self.env_stack):
                        pass

                    if self.env_stack == env:
                        match_found = True
                        call_index = matching_pattern_indices[i]
                        break

                
                if match_found == False: #If direct matches are not found move up the env_stack
                    for i, env in enumerate(definition_envs):
                        caller_env: list[str] = copy.deepcopy(self.env_stack) #the env where the call happened

                        if len(caller_env) < len(env):
                                pass
                        
                        for _ in range(len(caller_env)): 
                            if env == caller_env:
                                match_found = True
                                call_index = matching_pattern_indices[i]
                                break
                            else:
                                caller_env.pop()
                        
                        if match_found == True:
                            self.env_stack = caller_env
                            break
                
                #If none of the called patterns are available to the caller throw error
                if match_found == False:
                    raise ValueError(f"execute: the pattern {token} is out of scope.")
                        
                #Once the call has been made enter the caller env
                self.env_stack.append(token)
                
                #recursive self call to execute in-pattern sub-instructions
                #matched_call_index: int = matching_pattern_indices[call_index]
                sub_instructions: list[str] = self.pattern_lst[call_index].value
                self.replace_pattern_call(input_instruction_list = sub_instructions, output_instruction_list = output_instruction_list)
                
                #Once the call has finished pop the instruction pointer from the call stack
                self.call_stack.pop()

                #Once the call has finished leave the caller env
                if len(self.env_stack) > 1:
                    self.env_stack.pop()

            else:
                output_instruction_list.append(token)

            lp +=1



    def convert_to_raw(self, token_list: list[str], instruction_list: list[str] | None = None, start_index: int = 0, in_pattern: bool = False, in_loop: bool = False) -> None:
        tokens: list[str] = copy.deepcopy(token_list)
        local_loop_map: dict[int, int] = {}

        if in_pattern == False:
            instruction_list: list[str] = self.instruction_lst
            
            if len(self.loop_map) == 0:
                self.map_loops(token_list = tokens, sub_loop = False)
            
            self.map_patterns()
        
        else:
            instruction_list: list[str] | None = instruction_list

        if in_loop == True:
            local_loop_map = self.map_loops(token_list = tokens, sub_loop = True)
            
        lp: int = start_index
        while lp < len(tokens):
            token: str = tokens[lp]


            if re.match(pattern = "[FLR][0-9]+", string = token) or re.match(pattern = "[FLR]", string = token):
                instruction: str = re.split(pattern = "[0-9]", string = token, maxsplit = 2)[0]
                repeat: str = re.split(pattern = "[A-Z]", string = token, maxsplit = 2)[1]

                if repeat.isnumeric():
                    repeat_n: int = int(repeat)

                else:
                    repeat_n: int = 1

                for _ in range(repeat_n):
                    instruction_list.append(instruction)

            elif token == "(":
                loop_start: int = lp

                if in_loop == False:
                    loop_end: int = self.loop_map[lp]
                
                else:
                    loop_end: int = local_loop_map[lp]
                
                loop_slice: slice = slice(loop_start + 1, loop_end)
                loop_inst: list[str] = tokens[loop_slice]

                end_token: str = tokens[loop_end]
                repeat: str = re.split(pattern = "[)]", string = end_token, maxsplit = 2)[1]

                if repeat.isnumeric():
                    repeat_n: int = int(repeat)

                else:
                    repeat_n: int = 1

                for _ in range(repeat_n):
                    self.convert_to_raw(token_list = loop_inst, instruction_list = instruction_list, in_loop = True, in_pattern = in_pattern)

                lp = loop_end

            elif re.match(pattern = "[)][0-9]+", string = token) or re.match(pattern = "[)]", string = token):
                pass

            elif re.match(pattern = "[p][0-9]+", string = token):
                if len(self.env_stack) < 1:
                    raise ValueError(f"parser: the env_stack is {len(self.env_stack)} when it should be 1.")

                #Transfer ownership of the env_stack
                parent_env: list[str] = copy.deepcopy(self.env_stack)

                #Define the call ID for the defined pattern
                p_id: str = re.split(pattern = "p", string = token, maxsplit = 2)[1]
                pattern_ID: str = "P" + p_id
                
                #Push the pattern ID to the env stack
                self.env_stack.append(pattern_ID)

                #Define the local env (the env inside the pattern)
                local_env: str = self.env_stack[-1]
            
                #Define a new instruction list for the recursive parser call
                instr_lst: list[str] = []
                
                #If another pattern definition is found nested inside the previous definition, call the parser recursively
                self.convert_to_raw(token_list = tokens, instruction_list = instr_lst, start_index = lp + 1, in_pattern = True)

                #Pattern name duplication check
                for p in self.pattern_lst:
                    if p.name == pattern_ID and len(p.parent_scope) == len(parent_env) and p.parent_scope[-1] == parent_env[-1]:
                        raise ValueError(f"parser: the pattern ID: {pattern_ID} already exists in this environment {parent_env[-1]} and cannot be defined again.")
                
                #Create the new pattern definition with the associated instructions and push it onto the pattern list    
                self.pattern_lst.append(Pattern(name = pattern_ID, value = instr_lst, local_scope = local_env, parent_scope = parent_env)) 
                
                #When a pattern is fully defined jump over the definition to continue with the parsing
                lp = self.pattern_map[lp] 

            elif re.match(pattern = "q", string = token) and in_pattern == True:
                self.env_stack.pop()
                break

            elif re.match(pattern = "q", string = token) and in_pattern == False:
                pass

            elif re.match(pattern = "[P][0-9]+", string = token):
                instruction_list.append(token)
            
            lp += 1

            
        if in_pattern == False and in_loop == False:
            self.map_pattern_envs()
            self.replace_pattern_call(input_instruction_list = instruction_list, output_instruction_list = self.output_list)

        return self.output_list

pattern: str = """
p2017
  (
    P666 P1024
  )4
q
p1024
  p666
    p1024
      p666
        p1024
          L
        q

        F P1024
      q

      F P666
    q

    F P1024
  q

  F P666
q
p666
  p1024
    p666
      p1024
        p666
          R
        q

        F P666
      q

      F P1024
    q

    F P666
  q

  F P1024
q

P2017
"""

pattern2: str = "p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3qP0P1P2P3P4"

pattern3: str = """
p0
  p2
    p0
      (
        P1
      )2
    q

    (
      P0
    )2
  q

  (
    P2
  )
q

(
  P0
)

p1
  F7 R
q
"""



test: RSUProgram = RSUProgram(pattern3)
test.get_tokens()
test.convert_to_raw(test.token_lst)