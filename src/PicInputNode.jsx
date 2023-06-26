/* eslint-disable no-unused-vars */
import React, { memo } from 'react';
import { Handle, Position } from 'reactflow';

export default memo(({ data, isConnectable }) => {

  return (
    <>
      <Handle
        type="target"
        position={Position.Top}
        id="PicIN"
        isConnectable={isConnectable}
      />
      <div className='DefaultNode'>
        {data.label}
        <img src={data.sor} height={100} width={100} />
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        id="PicOUT"
        isConnectable={isConnectable}
      />
    </>
    );
});