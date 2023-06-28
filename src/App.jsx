/* eslint-disable no-unused-vars */
import React from 'react';
import ReactFlow, {
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  ReactFlowProvider,
} from 'reactflow';

import 'reactflow/dist/style.css';
import './App.css';
import pic from './000039220015.jpg';
import PicInputNode from './PicInputNode';
import CondiNode from './CondiNode';
import ElNode from './ElNode';
import FloNode from './FloNode'


const nodeTypes = {
  PicNode: PicInputNode,
  ConditionNode: CondiNode,
  ElseNode: ElNode,
  FloatNode: FloNode
};

const edgemarker = {type:'arrowclosed', width: 20, height:30}

const initialNodes = [{ id: 'PicInput', position: { x: 0, y: -100}, data: { label: 'Input:' , sor: pic}, type:'PicNode' },
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
const initialEdges = [{ id: 'ePicInput-cond3' , source: 'PicInput', target: 'cond3' , markerEnd: edgemarker,  type: 'smoothstep'},
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


export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  return(
  <div className="providerflow">
    <ReactFlowProvider>
      <div className="reactflow-wrapper" style={{ width: '100vw', height: '100vh' }}>
        <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            nodeTypes={nodeTypes}
            fitView
          >
            <Controls />
            <Background variant="dots" gap={12} size={1} />
        </ReactFlow>
      </div>
      <aside>
        <div className= "title">
          {'This is String'}
        </div>
        <img src={pic} height={100} width={100} />
      </aside>
    </ReactFlowProvider>
  </div>);

}