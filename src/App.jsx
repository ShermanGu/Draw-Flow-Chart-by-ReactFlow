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
import dagre from "dagre";

import 'reactflow/dist/style.css';
import './App.css';
import data1 from './test1.json';
import data2 from './test2.json';

import PicInputNode from './PicInputNode';
import RegularNode from './RegularNode';
import StmtNode from './StmtNode';

import FloNode from './FloNode';
import process from './process';


const nodeTypes = {
  PicNode: PicInputNode,
  RegulNode: RegularNode,
  StmtNode: StmtNode,
  FloatNode: FloNode
};


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

const [  initialNodes1,  initialEdges1 ] = process(data1);
const [  initialNodes2,  initialEdges2 ] = process(data2);


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