import React, {useState} from 'react';
import { Handle, Position } from 'reactflow';

function FloNode ({ data, isConnectable }){
    const [Hover,setHover] = useState(false)

    const handleMouseEnter = () => {
        setHover(true);
      };
    
    const handleMouseLeave = () => {
        setHover(false);
    };

  return (
    <div className='FloatNode'>
      <Handle
        type="target"
        position={Position.Top}
        id="target"
        isConnectable={isConnectable}
      />
      <b onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} className="withpre">
        {Hover ? Text(data) : data.label }
      </b>
      <Handle
        type="source"
        position={Position.Bottom}
        id="source"
        isConnectable={isConnectable}
      />
    </div>
    );
};

function Text(data){
    const input = data.input
    let str = []
    for(let i = 0; i < input.length; i++){
        str.push(<div>{"Parameter" + (String)(i+1) + ": " + input[i]}</div>)
    }
    return str
}

export default FloNode;