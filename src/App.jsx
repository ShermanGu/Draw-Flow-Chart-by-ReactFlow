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


const [  initialNodes1,  initialEdges1 ] = process(data);



console.log(initialNodes1)
console.log(initialEdges1)

export default function App() {

  const [nodes1, setNodes1, onNodesChange1] = useNodesState(initialNodes1);
  const [edges1, setEdges1, onEdgesChange1] = useEdgesState(initialEdges1);

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