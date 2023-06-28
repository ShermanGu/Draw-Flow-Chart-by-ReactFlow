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

const initialNodes = [{ id: 'op2', position: { x: 0, y: 100}, data: { label: ' output_grid = np.zeros((9, 9))' }, type: 'input' },
{ id: 'op4', position: { x: -86, y: 200}, data: { label: ' remove_grey_input_grid = remove_rows_cols(input_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'op6', position: { x: -86, y: 300}, data: { label: ' sub_blocks = separate_sub_blocks(remove_grey_input_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'op8', position: { x: -86, y: 400}, data: { label: ' output_block = find_block_with_4_non_black_elements(sub_blocks)', input:['sub_blocks: List[np.ndarray]']}, type: 'FloatNode' },
{ id: 'op10', position: { x: -86, y: 500}, data: { label: ' output_grid = set_block_colors(output_grid, output_block)', input:['output_grid: np.ndarray','output_block: np.ndarray']}, type: 'FloatNode' },
{ id: 'op12', position: { x: -86, y: 600}, data: { label: ' output_grid = add_grey_lines(output_grid)', input:['input_grid: np.ndarray']}, type: 'FloatNode' },
{ id: 'io17', position: { x: 0, y: 700}, data: { label: 'Output:' , sor: pic}, type:'PicNode' },
{ id: 'e15', position: { x: 0, y: 900}, data: { label: ' end function return' }, type: 'output' },
];
const initialEdges = [{ id: 'eop2-op4' , source: 'op2', target: 'op4' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop4-op6' , source: 'op4', target: 'op6' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop6-op8' , source: 'op6', target: 'op8' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop8-op10' , source: 'op8', target: 'op10' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop10-op12' , source: 'op10', target: 'op12' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop12-io17' , source: 'op12', target: 'io17' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eio17-e15' , source: 'io17', target: 'e15' , markerEnd: edgemarker,  type: 'smoothstep'},
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