import React, { useState } from 'react';
import ReactFlow, {
  ConnectionLineType,
  useNodesState,
  useEdgesState
} from "reactflow";
import dagre from "dagre";

import "reactflow/dist/style.css";

const dagreGraph = new dagre.graphlib.Graph();
dagreGraph.setDefaultEdgeLabel(() => ({}));

const nodeWidth = 172;
const nodeHeight = 36;

const getLayoutedElements = (nodes, edges, direction = "TB") => {
  const isHorizontal = direction === "LR";
  dagreGraph.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: nodeWidth, height: nodeHeight });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  nodes.forEach((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    node.targetPosition = isHorizontal ? "left" : "top";
    node.sourcePosition = isHorizontal ? "right" : "bottom";

    // We are shifting the dagre node position (anchor=center center) to the top left
    // so it matches the React Flow node anchor point (top left).
    node.position = {
      x: nodeWithPosition.x - nodeWidth / 2,
      y: nodeWithPosition.y - nodeHeight / 2
    };

    return node;
  });

  return { nodes, edges };
};

export default function process(data){
    var i;
    var initialNodes = [],initialEdges = [];
    for(i = 0; i< data.nodes.length; i++){
        initialNodes = initialNodes.concat([{id: data.nodes[i].id, position:{x:0,y:0}, data:{label: '1'}}])    
    }
    for(i = 0; i< data.edges.length; i++){
        initialEdges = initialEdges.concat([{ id: ('e' + data.edges[i][0] + '-' + data.edges[i][1]), source: data.edges[i][0], target:  data.edges[i][1], type: 'smoothstep'}])    
    }


    const { nodes: layoutedNodes, edges: layoutedEdges } = getLayoutedElements(
        initialNodes,
        initialEdges
      );
    

    return [layoutedNodes,layoutedEdges]
}



