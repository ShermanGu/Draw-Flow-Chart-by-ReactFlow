import React, {useState} from 'react';
import { Handle, Position } from 'reactflow';

function StmtNode ({ data, isConnectable }){
  return (
    <div className='DefaultNode'>
      <Handle
        type="target"
        position={Position.Top}
        id="target"
        isConnectable={isConnectable}
      />
      <div className = 'StmtBlock'> {data.label}</div>
      <div className = 'NaturalBlock'> " "</div>
      <Handle
        type="source"
        position={Position.Bottom}
        id="source"
        isConnectable={isConnectable}
      />
    </div>
    );
};

export default StmtNode;