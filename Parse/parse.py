import numpy as np
from pyflowchart import Flowchart

def parse(code,file,fun_name_list):
    nodes = None
    jsx_nodes = "const initialNodes = ["
    edges = None
    jsx_edges = "const initialEdges = ["
    lines = None
    if "'" in file:
        lines = file.split('\n')[1:]
    else:
        lines = file.split('\n')
    ConditionYCor = []
    # The Y-Cooridinate of The condition Node, store it in the list that can align the if-no node
    ElseNodes = []
    # The Node that only visits when if is false
    RePositionNodes = []
    # Nodes need to be reposition due to the overlapping edges (Nodes right after ElseNode)
    FunctionNodes = []
    # Nodes that are FloatNode / Function Node


    for i in range(len(lines)):
        if lines[i] == '':
            nodes = lines[:i]
            edges = lines[i+1:]
            break
    
    counter = 0
    else_operation = None
    for n in range(len(nodes)):
        counter += 1
        temp = nodes[n].split("=>")
        temp2 = temp[1].split(':')
        if(check_fun_name(temp2[1],fun_name_list)):
            FunctionNodes += [temp[0]]
            jsx_nodes += "{ id: '" + temp[0] + "', position: { x: -86, y: " + str(counter*100)
            fun_name = check_fun_name(temp2[1],fun_name_list)[0] # TODO Multiple function name in one line
            jsx_nodes += "}, data: { label: '" + temp2[1] + "', " + get_para(code,fun_name,fun_name_list) +"}, type: 'FloatNode' },\n"
        else:
            jsx_nodes += "{ id: '" + temp[0] + "', position: { x: 0, y: " + str(counter*100)
            if(temp2[0] == "inputoutput"):
                if temp2[1] == " input":
                    jsx_nodes += "}, data: { label: 'Input:' , sor: pic}, type:'PicNode' },\n"
                    counter += 1
                else:
                    jsx_nodes += "}, data: { label: 'Output:' , sor: pic}, type:'PicNode' },\n" 
                    counter += 1           
            elif(temp2[0] == "condition"):
                ConditionYCor += [(counter*100)]
                jsx_nodes += "}, data: { label: '" + temp2[1] + "' }, type: 'ConditionNode' },\n"
            elif(temp2[0] == "end"):
                jsx_nodes += "}, data: { label: '" + temp2[1] + "' }, type: 'output' },\n"
                else_operation = nodes[n+1:]
                break
            elif(counter == 1):
                jsx_nodes += "}, data: { label: '" + temp2[1] + "' }, type: 'input' },\n"
            else:
                jsx_nodes += "}, data: { label: '" + temp2[1] + "' } },\n"
    
    counter = 0
    if else_operation:
        for else_node in else_operation:
            temp = else_node.split("=>")
            ElseNodes += [temp[0]]
            jsx_nodes += "{ id: '" + temp[0] + "', position: { x: " + (str)((counter+1)*200) + ", y: " + (str)(ConditionYCor[len(else_operation) - 1 - counter])
            temp2 = temp[1].split(':')
            jsx_nodes += "}, data: { label: '" + temp2[1] + "' }, type: 'ElseNode' },\n"
            counter += 1

    jsx_nodes += "];"



    RePositionNodes = [-1]*(len(ElseNodes))

    for e in edges:
        YesOrNo = None
        temp = e.split("->")
        if len(temp) != 1:
            temp2 = temp[0].replace('(','&').replace(')','&').split('&')
            if len(temp2) != 1:
                YesOrNo = temp2[1]
            
            if(YesOrNo):
                source = temp2[0]
                target = temp[1]
                if(YesOrNo == 'yes'):
                    source_id = "CondiOUTbottom"
                else:
                    source_id = "CondiOUTright"
                jsx_edges += "{ id: 'e" + source + "-" + target + "(" + YesOrNo + ")" + "' , source: '" + source + "', target: '" + target
                jsx_edges += "' ," + "sourceHandle: '" + source_id + "', label: '" + YesOrNo + "', markerEnd: edgemarker,  type: 'smoothstep'},\n"

            else:
                source = temp[0]
                target = temp[1]
                if source in ElseNodes:
                    i = first_Indexof(ElseNodes,source)
                    RePositionNodes[i] = target
                jsx_edges += "{ id: 'e" + source + "-" + target + "' , source: '" + source + "', target: '" + target
                jsx_edges += "' , markerEnd: edgemarker,  type: 'smoothstep'},\n"


    jsx_edges += "];"
    temp_re = jsx_nodes + '\n' + jsx_edges
    
    
    
    # Needs to revise the node position so that edges do not overlap
    for counter in range(len(RePositionNodes)):
        if RePositionNodes[counter] in FunctionNodes:
            target_str = "{ id: '" + RePositionNodes[counter] + "', position: { x: -86"
            change_to = "{ id: '" + RePositionNodes[counter] + "', position: { x: " + (str)((counter+1)*200 - 86)
            temp_re = temp_re.replace(target_str,change_to)
        else:
            target_str = "{ id: '" + RePositionNodes[counter] + "', position: { x: 0"
            change_to = "{ id: '" + RePositionNodes[counter] + "', position: { x: " + (str)((counter+1)*200)
            temp_re = temp_re.replace(target_str,change_to)
    return temp_re


def first_Indexof(ls,ele):
    for i in range(len(ls)):
        if ls[i] == ele:
            return i
    return -1

def get_fun_names(code):
    temp1 = code.split('\n')
    temp2 = []
    re = []
    for t in temp1:
        if t[:3] == "def":
            temp2 += [t]
    for i in temp2:
        re += [i.replace('(', ' ').split(' ')[1]]
    return re

def check_fun_name(strls,fun_names):
    re_ls = []
    for n in fun_names:
        if n in strls:
            re_ls += [n]
    if re_ls == []:
        return None
    else:
        return re_ls

def get_para(code,fun_name,fun_names):
    temp1 = code.split('\n')
    temp2 = []
    re = []
    for t in temp1:
        if t[:3] == "def":
            temp2 += [t]
    for i in temp2:
        temp3 = i.replace('(', '#').replace(')','#').split('#')[1]
        re += [rmv_space(conditional_split(',',temp3))]
    index = first_Indexof(fun_names,fun_name)
    in_str = "input:['"
    for i in re[index]:
        in_str += i + "','"
    final_re = in_str[:-2] + ']'

    return final_re

def conditional_split(ele,strls):
    re = []
    window = len(ele)
    rest = strls
    start = 0
    flag = 0
    for i in range(len(strls)):
        if strls[i:i+window] == ele and flag == 0:
            re += [strls[start:i]]
            start = i+window
            rest = strls[i+window:]
        elif strls[i] == '[':
            flag += 1
        elif strls[i] == ']':
            flag -= 1
    re += [rest]
    return re

def rmv_space(ls):
    re = []
    for e in ls:
        temp = e
        counter = 0
        while e[counter] == ' ':
            temp = e[counter+1:]
            counter += 1
        pivot = len(temp) - 1
        temp2 = temp
        while temp[pivot] == ' ':
            temp2 = temp[:pivot]
            pivot -= 1
        re += [temp2]
    return re

with open('test.py') as f:
    code = f.read()
fc = Flowchart.from_code(code, field="main")
print(fc.flowchart())
print(parse(code,fc.flowchart(),get_fun_names(code)))

