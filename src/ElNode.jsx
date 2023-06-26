import React, { memo } from 'react';
import { Handle, Position } from 'reactflow';

export default memo(({ data, isConnectable }) => {

  return (
    <div className='DefaultNode'>
      <Handle
        type="target"
        position={Position.Left}
        id="CondiIN"
        isConnectable={isConnectable}
      />
      <div>
        {data.label}
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        id="CondiOUT1"
        isConnectable={isConnectable}
      />
    </div>
    );
});