export const numberToColor = number => {
    const colors = [
      "#000000",
      "#0000FF",
      "#FF0000",
      "#008000",
      "#FFFF00",
      "#808080",
      "#FFC0CB",
      "#FFA500",
      "#FFFF00",
      "#800000"
    ]
  
    return colors[number % 10]
  }
  
  export const colorToNumber = color => {
    const colors = [
      "#000000",
      "#0000FF",
      "#FF0000",
      "#008000",
      "#FFFF00",
      "#808080",
      "#FFC0CB",
      "#FFA500",
      "#FFFF00",
      "#800000"
    ]
  
    return colors.indexOf(color)
  }
  