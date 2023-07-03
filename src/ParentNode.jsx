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
      <div>
        {data.label}
      </div>
      <Handle
        type="source"
        position={Position.Left}
        id="LeftEdge"
        isConnectable={isConnectable}
      />
      <Handle
        type="source"
        position={Position.Right}
        id="RightEdge"
        isConnectable={isConnectable}
      />
    </div>
    );
});