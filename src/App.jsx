/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import ReactFlow, {
  ConnectionLineType,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  ReactFlowProvider,

} from 'reactflow';

import 'reactflow/dist/style.css';
import './App.css';
import data from './flow.json';
import pic from './000039220015.jpg';

import PicInputNode from './PicInputNode';
import ParentNode from './ParentNode';
import FloNode from './FloNode';
import process from './process';


const nodeTypes = {
  PicNode: PicInputNode,
  ParentNode: ParentNode,
  FloatNode: FloNode
};



const edgemarker = {type:'arrowclosed', width: 20, height:30}

const initialNodes1 = [{ id: 'PicInput', position: { x: 0, y: -100}, data: { label: 'Input:' , sor: pic}, type:'PicNode' },
{ id: 'cond3', position: { x: 0, y: 100}, data: { label: ' if input_grid' }, type: 'ConditionNode' },
{ id: 'sub7', position: { x: 0, y: 200}, data: { label: ' print(1)' } },
{ id: 'op14', position: { x: 200, y: 300}, data: { label: ' output_grid = np.zeros((9, 9))' } },
{ id: 'op16', position: { x: -86, y: 400}, data: { label: ' remove_grey_input_grid = remove_rows_cols(input_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'op18', position: { x: -86, y: 500}, data: { label: ' sub_blocks = separate_sub_blocks(remove_grey_input_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'op20', position: { x: -86, y: 600}, data: { label: ' output_block = find_block_with_4_non_black_elements(sub_blocks)', input:['sub_blocks: List[np.ndarray]']}, type: 'FloatNode' },
{ id: 'op22', position: { x: -86, y: 700}, data: { label: ' output_grid = set_block_colors(output_grid, output_block)', input:['output_grid: np.ndarray','output_block: np.ndarray']}, type: 'FloatNode' },
{ id: 'op24', position: { x: -86, y: 800}, data: { label: ' output_grid = add_grey_lines(output_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'io29', position: { x: 0, y: 900}, data: { label: 'Output:' , sor: pic}, type:'PicNode' },
{ id: 'e27', position: { x: 0, y: 1100}, data: { label: ' end function return' }, type: 'output' },
{ id: 'sub11', position: { x: 200, y: 100}, data: { label: ' print(2)' }, type: 'ElseNode' },
];
const initialEdges1 = [{ id: 'ePicInput-cond3' , source: 'PicInput', target: 'cond3' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd3-sub7(yes)' , source: 'cond3', target: 'sub7' ,sourceHandle: 'CondiOUTbottom', label: 'yes', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'esub7-op14' , source: 'sub7', target: 'op14' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop14-op16' , source: 'op14', target: 'op16' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop16-op18' , source: 'op16', target: 'op18' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop18-op20' , source: 'op18', target: 'op20' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop20-op22' , source: 'op20', target: 'op22' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop22-op24' , source: 'op22', target: 'op24' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop24-io29' , source: 'op24', target: 'io29' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eio29-e27' , source: 'io29', target: 'e27' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd3-sub11(no)' , source: 'cond3', target: 'sub11' ,sourceHandle: 'CondiOUTright', label: 'no', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'esub11-op14' , source: 'sub11', target: 'op14' , markerEnd: edgemarker,  type: 'smoothstep'},
];


function handleClick1(subtabid){
  var i,subtab;

  subtab = document.getElementsByClassName("subtab");
  for (i = 0; i < subtab.length; i++) {
    subtab[i].style.display = "none";
  }

  document.getElementById(subtabid).style.display = "block";
}

function handleClick2(graphid){
  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  document.getElementById(graphid).style.display = "block";
}


const [  initialNodes2,  initialEdges2 ] = process(data);



console.log(initialNodes2)
console.log(initialEdges2)

export default function App() {

  const [nodes1, setNodes1, onNodesChange1] = useNodesState(initialNodes1);
  const [edges1, setEdges1, onEdgesChange1] = useEdgesState(initialEdges1);
  const [nodes2, setNodes2, onNodesChange2] = useNodesState(initialNodes2);
  const [edges2, setEdges2, onEdgesChange2] = useEdgesState(initialEdges2);

  return(
  <div className = "body">
    <div id = "1" className='tabcontent'>
      <ReactFlowProvider>
        <div className="providerflow">
          <div className="reactflow-wrapper">
            <ReactFlow
              nodes={nodes1}
              edges={edges1}
              onNodesChange={onNodesChange1}
              onEdgesChange={onEdgesChange1}
              nodeTypes={nodeTypes}
              fitView
              >
              <Controls />
              <Background variant="dots" gap={12} size={1} />
            </ReactFlow>
          </div>
        </div>
      </ReactFlowProvider>
    </div>

    <div id = "2" className='tabcontent'>
      <ReactFlowProvider>
        <div className="providerflow">
          <div className="reactflow-wrapper">
            <ReactFlow
              nodes={nodes2}
              edges={edges2}
              onNodesChange={onNodesChange2}
              onEdgesChange={onEdgesChange2}
              nodeTypes={nodeTypes}
              fitView
              >
              <Controls />
              <Background variant="dots" gap={12} size={1} />
            </ReactFlow>
          </div>
        </div>
      </ReactFlowProvider>
    </div>


    <div className='title'>
      <h1>DataFlow Presentation</h1>
    </div>

    <div className = 'tab'>
      
      <button className="tablinks" onClick={() => handleClick1("tab1")}>1
        <div id = "tab1" className = "subtab"> 
          <button className="tablinks" onClick={() => handleClick2("1")}>1</button>
        </div>
      </button>

      <button className="tablinks" onClick={() => handleClick1("tab2")}>2
        <div id = "tab2" className = "subtab"> 
          <button className="tablinks" onClick={() => handleClick2("2")}>2</button>
        </div>
      </button>


    </div>

    <Helmet>
      <script>
        {'var i, tabcontent, subtab; tabcontent = document.getElementsByClassName("tabcontent"); for (i = 0; i < tabcontent.length; i++) {tabcontent[i].style.display = "none";} subtab = document.getElementsByClassName("subtab");for (i = 0; i < subtab.length; i++) {subtab[i].style.display = "none";}'}
      </script>
    </Helmet>
  </div>
  
  
  
  );

}