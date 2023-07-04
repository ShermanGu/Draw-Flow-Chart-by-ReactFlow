/* eslint-disable no-unused-vars */
import React, {useState} from 'react';
import { Handle, Position } from 'reactflow';
import { Box } from '@mui/material';
import { numberToColor } from './color';
import { Grid } from '@mui/material';

const size = 10;

function StringToArray(str){
  var i,flag;
  var re = [];
  var temp = [];
  flag = 0;
  for(i = 0;i<str.length;i++){
    if(str.charAt(i) == '['){
      flag ++
    }else if(str.charAt(i) == ']'){
      flag --
    }else if(str.charAt(i) == '\n'){
      re.push(temp)
      temp = [];
    }else if(str.charAt(i) == '1' && flag == 2){
      temp.push(1)
    }else if(str.charAt(i) == '2' && flag == 2){
      temp.push(2)
    }else if(str.charAt(i) == '3' && flag == 2){
      temp.push(3)
    }else if(str.charAt(i) == '4' && flag == 2){
      temp.push(4)
    }else if(str.charAt(i) == '5' && flag == 2){
      temp.push(5)
    }else if(str.charAt(i) == '6' && flag == 2){
      temp.push(6)
    }else if(str.charAt(i) == '7' && flag == 2){
      temp.push(7)
    }else if(str.charAt(i) == '8' && flag == 2){
      temp.push(8)
    }else if(str.charAt(i) == '9' && flag == 2){
      temp.push(9)
    }else if(str.charAt(i) == '0' && flag == 2){
      temp.push(0)
    }
    
  }
  return re;
}

const ColorBox = ({ color, size}) => {
  return (
    <Box
      sx={{
        width: size,
        height: size,
        backgroundColor: color,
        border: "1px solid black",
        cursor: "pointer"
      }}
    />
  )
}


function NumberToPic({data, isConnectable}){

  const grid = StringToArray(data.sor)

  return (
    <>
      <Handle
        type="target"
        position={Position.Top}
        id="PicIN"
        isConnectable={isConnectable}
      />
      <Grid item>
        <Box sx={{ display: 'flex', flexGrow: 1 }}>
          {grid.map((row, rowIndex) => (
            <div key={rowIndex}>
              {row.map((cell, colIndex) => (
                <ColorBox
                  key={colIndex}
                  color={numberToColor(cell)}
                  size={size}
                />
              ))}
            </div>
          ))}
        </Box>
      </Grid>

      <Handle
        type="source"
        position={Position.Bottom}
        id="PicOUT"
        isConnectable={isConnectable}
      />
    </>
    );
};

export default NumberToPic;