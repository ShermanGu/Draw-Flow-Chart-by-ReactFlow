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

const initialNodes = [{ id: 'op2', position: { x: -86, y: 100}, data: { label: ' a = deo(a, b)', input:['c','d']}, type: 'FloatNode' },
{ id: 'cond5', position: { x: 0, y: 200}, data: { label: ' if a' }, type: 'ConditionNode' },
{ id: 'cond10', position: { x: 0, y: 300}, data: { label: ' if b' }, type: 'ConditionNode' },
{ id: 'cond15', position: { x: 0, y: 400}, data: { label: ' if (a & b)' }, type: 'ConditionNode' },
{ id: 'op19', position: { x: 0, y: 500}, data: { label: ' a = (b + 1)' } },
{ id: 'op26', position: { x: 200, y: 600}, data: { label: ' b = 1' } },
{ id: 'op33', position: { x: 400, y: 700}, data: { label: ' a += 10' } },
{ id: 'io43', position: { x: 600, y: 800}, data: { label: 'Output:' , sor: pic}, type:'PicNode' },
{ id: 'e41', position: { x: 0, y: 1000}, data: { label: ' end function return' }, type: 'output' },
{ id: 'op23', position: { x: 200, y: 400}, data: { label: ' b = (a + 1)' }, type: 'ElseNode' },
{ id: 'op30', position: { x: 400, y: 300}, data: { label: ' a = 1' }, type: 'ElseNode' },
{ id: 'op37', position: { x: 600, y: 200}, data: { label: ' b += 1' }, type: 'ElseNode' },
];
const initialEdges = [{ id: 'eop2-cond5' , source: 'op2', target: 'cond5' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd5-cond10(yes)' , source: 'cond5', target: 'cond10' ,sourceHandle: 'CondiOUTbottom', label: 'yes', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd10-cond15(yes)' , source: 'cond10', target: 'cond15' ,sourceHandle: 'CondiOUTbottom', label: 'yes', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd15-op19(yes)' , source: 'cond15', target: 'op19' ,sourceHandle: 'CondiOUTbottom', label: 'yes', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop19-op26' , source: 'op19', target: 'op26' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop26-op33' , source: 'op26', target: 'op33' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop33-io43' , source: 'op33', target: 'io43' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eio43-e41' , source: 'io43', target: 'e41' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd15-op23(no)' , source: 'cond15', target: 'op23' ,sourceHandle: 'CondiOUTright', label: 'no', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop23-op26' , source: 'op23', target: 'op26' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd10-op30(no)' , source: 'cond10', target: 'op30' ,sourceHandle: 'CondiOUTright', label: 'no', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop30-op33' , source: 'op30', target: 'op33' , markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'econd5-op37(no)' , source: 'cond5', target: 'op37' ,sourceHandle: 'CondiOUTright', label: 'no', markerEnd: edgemarker,  type: 'smoothstep'},
{ id: 'eop37-io43' , source: 'op37', target: 'io43' , markerEnd: edgemarker,  type: 'smoothstep'},
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