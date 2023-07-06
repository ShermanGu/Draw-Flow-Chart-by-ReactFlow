import React, { memo } from 'react';
import { Handle, Position } from 'reactflow';

export default memo(({ data, isConnectable }) => {

  return (
    <div className='DefaultNode'>
      <Handle
        type="target"
        position={Position.Top}
        id="CondiIN"
        isConnectable={isConnectable}
      />
      <div className='Text'>
        {data.label}
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        id="LeftEdge"
        isConnectable={isConnectable}
      />
    </div>
    );
});